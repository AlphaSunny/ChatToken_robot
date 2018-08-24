import robot
from wxpy import *


if __name__ == "__main__":
    print("The robot is init")

    bot = Bot()
    robot = robot.Robot(bot)
    robot.start_broadcast_bot()
    robot.start_record_bot()
    robot.handle_add_friend()
    robot.start_auto_reply()


    print("hello world")

    embed()






