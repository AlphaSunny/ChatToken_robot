from speak import speaker
import time,datetime
import robot
from wxpy import *
import sched
import threading
from urllib import parse
from urllib import request
import json
import sys

class Robot(object):
    def __init__(self, bot):
        self.bot = bot

    def start_broadcast_bot(self):
        speak_sched = speaker.read_speaker_file('./speak/speak.txt')
        self.set_broadcast_bot(speak_sched)
        


    def send_message(self, group_name, msg):
        groups = self.bot.groups()
        group = groups.search(group_name)[0]
        group.send(msg)
        return True


    def set_broadcast_bot(self, sches):
        # 得到要向那个群发送什么信息
        for sche in sches:
            name = sche['group_nickname']
            send_time = sche['time']
            msg = sche['msg']
            #chat_robot.send_message(name, msg)

            # 得到要发送的时间和现在时间的间隔
            # 获取现在时间
            now_time = datetime.datetime.now()
            # 获取明天时间
            year = now_time.date().year
            month = now_time.date().month
            day = now_time.date().day
            # 获取明天3点时间
            next_time = datetime.datetime.strptime(str(year)+"-"+str(month)+"-"+str(day)+" " +send_time, "%Y-%m-%d %H:%M:%S")
            # # 获取昨天时间
            # last_time = now_time + datetime.timedelta(days=-1)
              
            timer_start_time = (next_time - now_time).total_seconds()
            if(timer_start_time<0):
                continue
            timer = threading.Timer(timer_start_time, self.send_message, (name, msg))
            timer.start()

        #print(timer_start_time)

    def start_record_bot(self):
        record_group = ensure_one(self.bot.groups().search('聊天机器人测试群'))
        @self.bot.register(record_group)
        def forward_boss_message(msg):
            timeArray = time.localtime(msg.raw['CreateTime'])
            sendTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print(msg.sender)
            print(msg.raw)
            params = parse.urlencode({'nickname': msg.raw['ActualNickName'], 'content': msg.text, 'send_time': sendTime})
            f = request.urlopen("http://bot.fnying.com/bot/collect_message.php?%s" % params)
            print(f.read())
      
    
    def handle_add_friend(self):
        @self.bot.register(msg_types=FRIENDS)
        def auto_accept_friends(msg):
            # 接受好友请求
            new_friend = msg.card.accept()
            params = parse.urlencode({'bot_nickname':'aaa'})
            f = request.urlopen("http://bot.fnying.com/bot/reg.php?%s" % params)
            data = f.read()
            js = json.loads(data.decode("utf-8"))
            new_friend.set_remark_name(js['bot_mark'])
            print(js['bot_mark'])
            print("你好，我是您的hivebanks小助手pool，欢迎加入，您的CCVT账户代码是" + str(js['bot_mark']))
            new_friend.send("你好，我是您的hivebanks小助手pool，欢迎加入，您的CCVT账户代码是" + str(js['bot_mark']))
            new_friend.send("输如‘ccvt’查询拥有数量，输入‘发言数’查询今日发言条数")
            


    def start_auto_reply(self):
        @self.bot.register(Friend, msg_types=TEXT)
        def auto_reply(msg):
            print(msg)
            print(msg.sender.remark_name)
            if "ccvt" in msg.text.lower():
                print("kaishile")
                params = parse.urlencode({'bot_mark': msg.sender.remark_name})
                data = request.urlopen("http://bot.fnying.com/bot/search_bot_amount.php?%s" % params).read()
                data_json = json.loads(data.decode("utf-8"))
                print(data_json)
                if(data_json["errcode"] == "101"):
                    return "对不起，找不到你的账户"
                elif (data_json["errcode"] == "0"):
                    return "恭喜你，你今天已经有" + str(data_json["base_amount"]) + "个ccvt了"
                else:
                    return "未知错误，请联系管理员"
                return 

            elif "发言数" in msg.text:
                print("yyy")
                params = parse.urlencode({'bot_nickname': msg.sender.remark_name})
                data = request.urlopen("http://bot.fnying.com/bot/search_day_message.php?%s" % params).read()
                data_json = json.loads(data.decode("utf-8"))
                if(data_json["errcode"] == "101"):
                    return "对不起，找不到你的账户"
                elif (data_json["errcode"] == "0"):
                    return "恭喜你，你今天已经有" + str(data_json["count"]) + "条发言了"
                else:
                    return "未知错误，请联系管理员"
            
            return 




# http://bot.fnying.com/bot/search_day_message.php?bot_nickname=128

# http://bot.fnying.com/bot/search_bot_amount.php?bot_mark=128