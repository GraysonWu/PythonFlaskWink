# !/usr/bin/python3
# -*- coding: utf-8 -*-
__author__ = "Jeako_Wu"

import utility
import sql
import MySQLdb
from passlib.hash import sha256_crypt

def register_process(user):

    # user password 加密
    user.password = sha256_crypt.hash(user.password)

    try:
        # 打开数据库连接
        db = MySQLdb.connect("localhost", "root", "wujiahao.", "flaskTest")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 生成SQL语句
        query = sql.insert('users', utility.class_2_dict(user))


        try:
            # 使用execute方法执行SQL语句
            cursor.execute(query)

            # 提交操作到db
            db.commit()

        except:
            # 操作失败回滚
            db.rollback()

            return "User already exist"

        # 关闭数据库连接
        db.close()

        return "Successfully Register"

    except:
        return "Unable to connect to DB"

