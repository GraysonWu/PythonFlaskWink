# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import os

from flask import Flask, request, Response


import entities
import utility, db_link
import json

from hd_base import require

from register_process import register_process
from login_process import login_process
from home_commodity import home_commodity
from commodity_detail import commodity_detail
from home_store import home_store
from vendor_op import vendor_exist, vendor_info, vendor_edit, vendor_total_info
from product_op import enter_spec, per_commoditys, enter_pdf, delete_product, get_price

from werkzeug.datastructures import Headers


class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        header = ('Access-Control-Allow-Headers', 'x-requested-with,content-type')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
            headers.add(*header)
        else:
            headers = Headers([origin, methods, header])
        kwargs['headers'] = headers
        return super().__init__(response, **kwargs)


UPLOAD_FOLDER = '/var/lib/tomcat7/webapps/ROOT/pdf'
# UPLOAD_FOLDER = '/Users/jeako/Desktop'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.response_class = MyResponse
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index/')
def index():
    return "<h>Hello World</h>"


@app.route('/signup', methods=['POST'])
@require('username', 'number', 'password', 'identity')
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    number = request.json.get("number")
    identity = request.json.get("identity")

    user = entities.User(username, number, password)

    result = register_process(user, identity)
    response = entities.ResponseClass(True, "", "null")

    response.msg = result[0]
    response.isSuccess = result[1]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

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

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

    return result


@app.route('/home/commodity', methods=['GET'])
def homecommodity():

    query = home_commodity()
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = query[0]
    response.msg = query[1]
    response.data = query[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


@app.route('/home/store', methods=['GET'])
def homestore():

    query = home_store()
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = query[0]
    response.msg = query[1]
    response.data = query[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


@app.route('/product/detail', methods=['GET'])
def per_commodity():
    id_get = request.args.get('id')

    result = commodity_detail(id_get)
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = result[0]
    response.msg = result[1]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


@app.route('/store/ifnew', methods=['GET'])
def query_vendor():
    name_get = request.args.get('name')

    result = vendor_exist(name_get)
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = result[0]
    response.msg = result[1]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


@app.route('/store/basicinfo', methods=['GET'])
def vendorinfo():
    name_get = request.args.get('name')

    result = vendor_info(name_get)
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = result[0]
    response.msg = result[1]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


@app.route('/store/editinfo', methods=['POST'])
def vendoredit():
    name = request.json.get("name")
    company = request.json.get("company")
    address = request.json.get("address")
    phone = request.json.get("phone")
    fax = request.json.get("fax")
    star = request.json.get("star")
    pic = request.json.get("pic")

    basicinfo = entities.Basicinfo(company, address, phone, fax, star, pic)

    result = vendor_edit(name, basicinfo)
    response = entities.ResponseClass(True, "", "null")

    response.msg = result[1]
    response.isSuccess = result[0]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

    return result


@app.route('/store/enterproduct/spec', methods=['POST'])
def enterspec():
    name = request.json.get("name")
    url = request.json.get("url")
    productId = request.json.get("productId")
    detail = request.json.get("detail")

    result = enter_spec(name, productId, detail, url)
    response = entities.ResponseClass(True, "", "null")

    response.msg = result[1]
    response.isSuccess = result[0]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

    return result


@app.route('/store/totalinfo', methods=['GET'])
def vendortotalinfo():
    name_get = request.args.get('name')

    result = vendor_total_info(name_get)
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = result[0]
    response.msg = result[1]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


@app.route('/store/showproduct/detail', methods=['GET'])
def perprovide():
    name_get = request.args.get('name')
    productId_get = request.args.get('productId')
    company_name = db_link.vendor_name2company_name(name_get)

    result = per_commoditys(company_name, productId_get)
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = result[0]
    response.msg = result[1]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


@app.route('/store/enterproduct/pdf', methods=['POST'])
def uploadpdf():
    name = request.form.get("name")
    productId = request.form.get("productId")
    file = request.files["file"]

    filename = ""
    if request.method == 'POST':
        if file and allowed_file(file.filename):
            filename = name
            filename += "_"
            filename += productId
            filename += ".pdf"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    pdf_path = "wink.net.cn:8000/pdf/" + filename
    result = enter_pdf(name, productId, pdf_path)
    response = entities.ResponseClass(True, "", "null")

    response.msg = result[1]
    response.isSuccess = result[0]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

    return result


@app.route('/store/deleteproduct', methods=['POST'])
def deleteproduct():
    name = request.json.get("name")
    productId = request.json.get("productId")

    result = delete_product(name, productId)
    response = entities.ResponseClass(True, "", "null")

    response.msg = result[1]
    response.isSuccess = result[0]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')

    return result


@app.route('/getPrice', methods=['GET'])
def getprice():
    company_name_get = request.args.get('companyName')
    productId_get = request.args.get('productId')
    spec_get = request.args.get('spec')

    result = get_price(company_name_get, productId_get, spec_get)
    response = entities.ResponseClass(True, "", "null")

    response.isSuccess = result[0]
    response.msg = result[1]
    response.data = result[2]

    resp_dict = utility.class_2_dict(response)
    result = json.dumps(resp_dict, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False).encode('utf8')
    return result


def main():
    # app.run(host='45.77.190.232', port=5000, debug=True)
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()
