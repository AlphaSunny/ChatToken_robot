import robot
from wxpy import *


if __name__ == "__main__":
    print("The robot is init")

    bot = Bot()
    robot = robot.Robot(bot)
    robot.start_broadcast_bot()
    
    print("hello world")



