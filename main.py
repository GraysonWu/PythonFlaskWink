# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"

from flask import Flask, request

import entities

from hd_base import require
from register_process import register_process
from login_process import  login_process
from update_userinfo_process import update_process

app = Flask(__name__)




@app.route('/')
@app.route('/index/')
def index():
    return "<h>ARE YOU OK</H>"


@app.route('/register/', methods=['POST'])
@require('name', 'phone_number', 'password')
def register():
    name = request.json.get("name")
    password = request.json.get("password")
    phone_number = request.json.get("phone_number")

    user = entities.User(name, phone_number, password)

    return register_process(user)


@app.route('/login/', methods=['POST'])
@require('account', 'password')
def login():
    account = request.json.get("account")
    password = request.json.get("password")

    return login_process(account, password)


@app.route('/update/', methods=['POST'])
@require('name', 'phone_number', 'password')
def update():
    name = request.json.get("name")
    password = request.json.get("password")
    phone_number = request.json.get("phone_number")

    user = entities.User(name, phone_number, password)
    return update_process(user)


def main():
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()
