import pymysql.cursors

import random
import string

def randomString(stringLength=45):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

host = "104.223.107.42"
#host = 'localhost'
#host = "34.97.131.241"
user = 'root'
password = 'amitpandey123121'
dab = 'psnchecker'

class DB:
    conn = None
    def connect(self):
        #self.conn = pymysql.connect(host = host,user = "amit",password = "amitpandey123121",db = "covid19bot")
        self.conn = pymysql.connect(host = host,user = user,password = password,db = dab)
    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql)
        return cursor
    def commit(self):
        try:
            self.conn.commit()
        except:
            self.connect()
            self.conn.commit()

db = DB()

def check_key(key):
    sql = "select * from license where code = '{}'".format(key)
    a = db.query(sql)
    b= a.fetchall()
    if b:
        return b[0]
    else:
        return False
    
def create_key(user):
    code = randomString()
    sql = "insert into license(created_by,code,used) values('{}','{}',0)".format(user,code)
    db.query(sql)
    db.commit()
    return code

def check_admin(user):
    sql = "select * from admins where user='{}'".format(user)
    a = db.query(sql)
    b= a.fetchall()
    if b:
        return True
    else:
        return False
