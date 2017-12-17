# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"

import sql
import pymysql
from passlib.hash import sha256_crypt


def login_process(number, password, identity):

    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 查询字段
        key = ["password"]

        # 查询条件
        condition = {'number': number}

        # 可以用phone number也可以用name登录
        # if '9' >= account[0] >= '0' or account[0] == '+':
        #     condition["number"] = account
        # else:
        #     condition["username"] = account

        # 生成SQL语句
        query = sql.select(identity, key, condition, 0)

        # 使用execute方法执行SQL语句
        if cursor.execute(query):
            # 获取结果
            result = cursor.fetchone()

            # 关闭数据库连接
            db.close()

            # 验证密码
            password_verified = sha256_crypt.verify(password, str(result[0]))

            if password_verified:

                return "登录成功", True

            else:

                return "密码错误", False

        else:
            return "用户不存在，请先注册", False


    except:

        return "Unable to connect to DB"
