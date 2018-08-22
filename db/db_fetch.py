from db import db_connect
def get_data():
    database = db_connect.connect_db()
    curser = database.cursor()
    curser.execute("select * from bot_send")
    data = curser.fetchone()
    return data


def get_send_data():
    database = db_connect.connect_db()
    curser = database.cursor()
    curser.execute("select * from bot_send")
    data = curser.fetchone()
    return data


def insert_bot_base():
    db = db_connect.connect_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO bot_base \
       VALUES ('%s', '%s', '%d', '%d', '%s' )" % \
       ('Mac', 'Mohan', 200, 4, 'yang')

    try:
        # 执行sql语句
        cursor.execute(sql)
        print("1")
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()



def update_bot_base():
    db = db_connect.connect_db()
    cursor = db.cursor()
    sql = "update bot_base set bot_nikename ='1' where us_id = '%s'" % ("yang")

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

def delete_bot_base():
    db = db_connect.connect_db()
    cursor = db.cursor()
    sql = "delete from bot_base where us_id = '%s'" % ("yang")

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()