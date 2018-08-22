'''
from wxpy import *

bot = Bot()

# 获取所有好友
friends = bot.friends()

# 遍历输出好友名称
for friend in friends:
    print(friend)


# 找到好友
friend = friends.search('Pool')[0]
print(friend)
friend.send("hello world!")



# 获取所有聊天群
groups = bot.groups()

for group in groups:
    print(group)

# 找到目标群
group = groups.search("聊天机器人测试群")[0]

group.send("hello world!")

'''