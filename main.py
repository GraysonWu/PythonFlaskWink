# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"

from flask import Flask, request

import entities
import utility

from hd_base import require
from register_process import register_process
from login_process import  login_process
from update_userinfo_process import update_process

app = Flask(__name__)




@app.route('/')
@app.route('/index/')
def index():
    return "<h>ARE YOU OK</H>"


@app.route('/register', methods=['POST'])
@require('username', 'number', 'password', 'identity')
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    number = request.json.get("number")
    identity = request.json.get("identity")

    user = entities.User(username, number, password)

    result = register_process(user, identity)
    response = entities.Response(True, "")

    response.msg = result[0]
    response.isSuccess = result[1]

    return str(utility.class_2_dict(response))


@app.route('/login', methods=['POST'])
@require('number', 'password', 'identity')
def login():
    number = request.json.get("number")
    password = request.json.get("password")
    identity = request.json.get("identity")

    result = login_process(number, password, identity)
    response = entities.Response(True, "")

    response.msg = result[0]
    response.isSuccess = result[1]

    return str(utility.class_2_dict(response))


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
