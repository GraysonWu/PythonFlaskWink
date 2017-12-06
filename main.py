# !/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "Jeako_Wu"

from flask import Flask, render_template

import entities
import sql
from register_process import register_process
from login_process import  login_process

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/register/')
def registerProcess():
    #TODO: set User with request

    #temp user
    name = "zhangqi"
    password = "123456"
    phone_number = "+8618819253694"

    user = entities.User(name, phone_number, password)

    return register_process(user)

@app.route('/login/')
def loginProcess():
    #TODO: get phone number and password from request

    #temp login try
    phone_number = "13609756780"
    password = "123456"

    return login_process(phone_number , password)

@app.route('/updateuserinfo/')
def updateuserinfoProcess():
    # Create cursor
    cur = mysql.connection.cursor()

    tablename = "users"
    value = {}
    value["username"] = "Wink"
    condition = {}
    condition["name"] = "zhangqi"

    query = sql.update(tablename, value, condition)

    result = cur.execute(query)

    # Commit to DB
    mysql.connection.commit()

    # Close connection
    cur.close()

    if result:
        return "Success"
    else:
        return "Fail"


def main():
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()


# CREATE TABLE users(id INT(20) AUTO_INCREMENT PRIMARY KEY , name VARCHAR(100)  UNIQUE,phone_number VARCHAR(20)  UNIQUE, password VARCHAR(100),register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)DEFAULT CHARSET=utf8;

