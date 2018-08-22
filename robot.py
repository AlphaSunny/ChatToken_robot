from db import db_fetch


class Robot(object):
    def __init__(self, bot):
        self.bot = bot

    '''
    def send_message_to_group(self):
        data = db_fetch.get_send_data()
        group = data[1]
        time = data[2]
        msg = data[3]
        result = self.send_message(group, time, msg)
        return result
    '''



    def send_message(self, group_name, msg):
        
        groups = self.bot.groups()
        for group in groups:
            print(group)
        group = groups.search(group_name)[0]
        group.send(msg)
        return True






