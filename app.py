import flask
from flask import *
from db import *

app = Flask(__name__, static_folder='./static')

@app.route('/check/<code>',methods = ['GET'])
def check(code):
    check = check_key(code)
    if check != False:
        key = check[2]
        is_used = check[3]
        if is_used:
            return 'False'
        else:
            sql = "update license SET used = 1 where code='{}'".format(code)
            db.query(sql)
            db.commit()
            return 'Success'
    else:
        return 'False'

@app.route('/create/<user>')
def create(user):
    a = check_admin(user)
    if a:
        code = create_key(user)
        return code
    else:
        return '''Error!'''

@app.route('/check_key/<code>')
def check_it(code):
    check = check_key(code)
    if check != False:
        return "Success"
    else:
        return 'Failed'

@app.route('/addadmin/thesudoamit/<user>')
def addd_Admin(user):
    sql = "insert into admins(user,sudo) values('{}',0)".format(user)
    db.query(sql)
    db.commit()
    return 'Success'