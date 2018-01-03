# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"


import utility
import sql
import pymysql
from passlib.hash import sha256_crypt


def register_process(user, identity):
    # user password 加密
    user.password = sha256_crypt.hash(user.password)

    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        key = ["id"]
        condition = {"username": user.username}
        query = sql.select(identity,key,condition,0)

        if cursor.execute(query):
            return "该用户名已经存在", False

        key = ["id"]
        condition = {"number": user.number}
        query = sql.select(identity, key, condition, 0)

        if cursor.execute(query):
            return "该手机号已经存在", False

        # 生成SQL语句
        query = sql.insert(identity, utility.class_2_dict(user))

        try:
            # 使用execute方法执行SQL语句
            cursor.execute(query)
            # 提交操作到db
            db.commit()
        except:
            # 操作失败回滚
            db.rollback()

            return "注册失败", False

        # 关闭数据库连接
        db.close()

        return "注册成功", True
    except:
        return "Unable to connect to DB", False

