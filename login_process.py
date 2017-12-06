# !/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "Jeako_Wu"

import sql
import MySQLdb
from passlib.hash import sha256_crypt

def login_process(phone_number , password):

    try:
        # 打开数据库连接
        db = MySQLdb.connect("localhost", "root", "wujiahao.", "flaskTest")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        key = ["password"]
        condition ={}
        condition["phone_number"] = phone_number

        # 生成SQL语句
        query = sql.select('users', key , condition , 0)

        # 使用execute方法执行SQL语句
        cursor.execute(query)

        # 获取结果
        result = cursor.fetchone()


        # 关闭数据库连接
        db.close()

        password_verified = sha256_crypt.verify(password, str(result[0]))

        if password_verified:

            return "Successfully Login"

        else:

            return "Wrong password or phone number"

    except:

        return "Unable to connect to DB"
