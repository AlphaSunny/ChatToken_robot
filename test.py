from speak import speaker
import time,datetime
from wxpy import *
import sched
import threading
import json

from urllib import parse
from urllib import request

'''

speak_sched = speaker.read_speaker_file('./speak/speak.txt')

timeArray = time.strptime(speak_sched[0]['time'], "%H:%M:%S")



def set_broadcast_bot(sche):
    bot = Bot()
    chat_robot = robot.Robot(bot)
    # 得到要向那个群发送什么信息
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
    timer = threading.Timer(timer_start_time, chat_robot.send_message, (name, msg))
    timer.start()

    print(timer_start_time)
    

    
    
set_broadcast_bot(speak_sched[0])



#print(time.time().tm_year)
'''
'''

timeStamp = 1534935544
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)   # 2013--10--10 15:40:00
# time获取当前时间戳
now = int(time.time())     # 1533952277
timeArray = time.localtime(1534935544)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)  
'''


'''
bot = Bot()
@bot.register()
def accept_msg(msg):
    print(msg.card)

embed()
'''

params = parse.urlencode({'bot_nickname':'aaa'})
f = request.urlopen("http://bot.fnying.com/bot/reg.php?%s" % params)
data = f.read()
print ('Retrieved',len(data),'characters')

js = json.loads(data.decode("utf-8"))

print(js['bot_mark'])