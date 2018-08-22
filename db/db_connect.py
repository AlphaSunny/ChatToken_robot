import pymysql

def connect_db():
    return pymysql.connect(host='47.106.113.240',
                           port=3306,
                           user='admin',
                           password='l4ly8hgd4cluk8s7',
                           database='DevHive',
                           charset='utf8')