from speak import speaker
import time,datetime
import robot
from wxpy import *
import sched
import threading


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

            # 获取距离明天3点时间，单位为秒
            timer_start_time = (next_time - now_time).total_seconds()
            timer = threading.Timer(timer_start_time, self.send_message, (name, msg))
            timer.start()

        #print(timer_start_time)





