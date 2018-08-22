from speak import speaker
import time,datetime
import robot
from wxpy import *
import sched
import threading


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
    

    s = sched.scheduler(time.time, time.sleep)
    s.enter(timer_start_time, 1, chat_robot.send_message, (name, msg) )
    print(timer_start_time)
    s.run()
    #定时器,参数为(多少时间后执行，单位为秒，执行的方法)
timer = threading.Timer(timer_start_time, func)
timer.start()
    

    
    
set_broadcast_bot(speak_sched[0])



#print(time.time().tm_year)