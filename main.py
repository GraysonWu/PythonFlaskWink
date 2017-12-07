# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"

from flask import Flask, render_template

import entities
import sql
from register_process import register_process
from login_process import  login_process
from update_userinfo_process import update_process

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/register/')
def registerProcess():
    #TODO: set User with request

    #temp user
    name = "wujiahao"
    password = "123456"
    phone_number = "13609756780"

    user = entities.User(name, phone_number, password)

    return register_process(user)

@app.route('/login/')
def loginProcess():
    #TODO: get account and password from request

    #temp login try
    account = "13609756780"
    password = "123456"

    return login_process(account , password)

@app.route('/updateuserinfo/')
def updateuserinfoProcess():
    #TODO: set User with request

    # temp user
    name = "wujiahao"
    password = "123456"
    phone_number = "13609756780"

    user = entities.User(name, phone_number, password)
    return update_process(user)



def main():
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()
