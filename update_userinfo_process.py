# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"

import sql
import pymysql
from passlib.hash import sha256_crypt


def update_process(user):

    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 查询字段
        value = {}
        value["phone_number"] = user.phone_number
        value["password"] = sha256_crypt.hash(user.password)

        # 更新条目
        condition = {}
        condition["name"] = user.name


        # 生成SQL语句
        query = sql.update("users", value, condition)


        try:
            # 使用execute方法执行SQL语句
            if cursor.execute(query):

                db.commit()

                return "Successfully update"

            else:

                return "Update failed"

        except:
            return "Error while update"


    except:

        return "Unable to connect to DB"
