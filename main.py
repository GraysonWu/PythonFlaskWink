# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"

from flask import Flask, request, Response, redirect, url_for

import entities
import utility
import json

from hd_base import require

from register_process import register_process
from login_process import login_process
from update_userinfo_process import update_process
from homedisplay import home_display
from commodity_detail import commodity_detail
from werkzeug.datastructures import Headers

class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        header = ('Access-Control-Allow-Headers','x-requested-with,content-type')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
            headers.add(*header)
        else:
            headers = Headers([origin, methods,header])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)


UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.response_class = MyResponse
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
@app.route('/index/')
def index():
    return "<h>ARE YOU OK</h>"


@app.route('/signup', methods=['POST'])
@require('username', 'number', 'password', 'identity')
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    number = request.json.get("number")
    identity = request.json.get("identity")

    user = entities.User(username, number, password)

    result = register_process(user, identity)
    response = entities.ResponseClass(True, "" ,"null")

    response.msg = result[0]
    response.isSuccess = result[1]

    result = json.dumps(utility.class_2_dict(response), sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False).encode('utf8')

    return result


@app.route('/login', methods=['POST'])
@require('number', 'password', 'identity')
def login():
    number = request.json.get("number")
    password = request.json.get("password")
    identity = request.json.get("identity")

    result = login_process(number, password, identity)
    response = entities.ResponseClass(True, "", "null")

    response.msg = result[0]
    response.isSuccess = result[1]
    response.data = result[2]

    result = json.dumps(utility.class_2_dict(response),sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

    return result


@app.route('/homedisplay',methods=['GET'])
def homedisplay():

    result = home_display()
    response = json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'),
                        ensure_ascii=False).encode('utf8')
    return response


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return "Success"


@app.route('/product/detail',methods=['GET'])
def per_commodity():
    id = request.args.get('id')

    result = commodity_detail(id)
    response = json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'),
                        ensure_ascii=False).encode('utf8')
    return response
def main():
    # app.run(host='45.77.190.232', port=5000, debug=True)
    app.run(host='127.0.0.1', port=8080, debug=True)

if __name__ == '__main__':
    main()