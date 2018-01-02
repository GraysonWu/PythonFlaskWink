# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql


def home_display():
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest",charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 查询字段
        key = ['id', 'name', 'pic_path']

        # 查询条件
        condition = {}

        # 生成SQL语句
        query = sql.select("commodity", key, condition, 0)

        # 使用execute方法执行SQL语句
        if cursor.execute(query):
            # 获取结果
            data = cursor.fetchall()

            result = []
            for row in data:
                dict_commo = {}
                dict_commo["id"] = row[0]
                dict_commo["name"] = row[1]
                # file = open(row[2], 'r')
                # base = file.read()
                # file.close()
                # dict_commo["base64"] = base

                result.append(dict_commo)
                break
            # 关闭数据库连接
            db.close()

            return result

        else:
            return "查询失败"


    except:
        return "无法连接数据库"
