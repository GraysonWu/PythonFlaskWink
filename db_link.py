# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql


def company_name2vendor_id(company_name):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest",charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        result = {}

        key = ['id', 'username']
        condition = dict()
        condition['company_name'] = company_name

        query = sql.select("vendor", key, condition, 0)

        if cursor.execute(query):
            info = cursor.fetchone()
            result["id"] = info[0]
            result["company_name"] = company_name


        db.close()
        return result
    except:
        return "无法连接数据库"


def commodity_id2company_name(id):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest",charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        stores = []
        key = ['company']
        condition = dict()
        condition['commodity_id'] = id

        query = sql.select("provide", key, condition, 0)

        if cursor.execute(query):
            info = cursor.fetchall()
            for row in info:
                stores.append(row[0])
        db.close()
        return stores

    except:
        return "无法连接数据库"


def commodity_id2commodity_name(id):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest",charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        result = dict()

        key = ['id','name']
        condition = dict()
        condition['id'] = id

        query = sql.select("commodity", key, condition, 0)

        if cursor.execute(query):
            info = cursor.fetchone()
            result['id'] = info[0]
            result['name'] = info[1]

        db.close()
        return result

    except:
        return "无法连接数据库"


def vendor_name2company_name(vendor_name):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest",charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        key = ['company_name']
        condition = dict()
        condition['username'] = vendor_name

        query = sql.select("vendor", key, condition, 0)

        if cursor.execute(query):
            info = cursor.fetchone()
            result = info[0]

        db.close()
        return result

    except:
        return "无法连接数据库"


def company_name2vendor_name(company_name):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        result = {}

        key = ['username']
        condition = dict()
        condition['company_name'] = company_name

        query = sql.select("vendor", key, condition, 0)

        if cursor.execute(query):
            info = cursor.fetchone()
            result["vendor"] = info[0]

        db.close()
        return result["vendor"]
    except:
        return "无法连接数据库"