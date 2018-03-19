# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql
from db_link import commodity_id2commodity_name, vendor_name2company_name


def enter_spec(name, commodityId, detail, url):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        company_name = vendor_name2company_name(name)
        # 查询条件
        condition = dict()
        condition['company'] = company_name
        condition['commodity_id'] = commodityId

        # 生成SQL语句
        query = sql.delete("provide", condition)

        # 使用execute方法执行SQL语句
        try:
            cursor.execute(query)
            db.commit()
            for obj in detail:
                condition = dict()
                condition["spec"] = obj["spec"]
                condition["price"] = obj["price"]
                condition["commodity_id"] = commodityId
                condition["pdf_path"] = url
                condition["company"] = company_name
                query = sql.insert("provide", condition)
                cursor.execute(query)
            db.commit()

        except:
            db.rollback()
            return False, "录入商品支数和价格失败", "null"

        db.close()
        return True, "录入商品支数和价格成功", "null"

    except:
        return False, "无法连接数据库" , "null"


def total_commoditys(company_name):
    try:
        total = list()
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
      
        key = ["id", "name"]
        condition = dict()

        query = sql.select("commodity", key, condition , 0)
        cursor.execute(query)

        commodities = cursor.fetchall()
        detail = list()
        for commodity in commodities:
            dp = per_commoditys(company_name, commodity[0])
            result = dict()
            if dp[0]:
                result["productId"] = commodity[0]
                result["productName"] = commodity[1]
                result["detail"] = dp[2]["detail"]
                result["pdf"] = dp[2]["pdf"]
                total.append(result)
        db.close()
        return total
    except:
        return False, "获取商家详细信息失败", "null"


def per_commoditys(company_name,commodity_id):
    try:
        result = dict()
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        key = ["spec", "price", "pdf_path"]

        condition = dict()
        condition["company"] = company_name
        condition["commodity_id"] = commodity_id

        query = sql.select("provide", key, condition, 0)
        detail = list()
        if cursor.execute(query):
            details = cursor.fetchall()
            pdf_path = details[0][2]

            for sp in details:
                per_sp = dict()
                per_sp["spec"] = sp[0]
                per_sp["price"] = sp[1]
                detail.append(per_sp)

            result["detail"] = detail
            result["pdf"] = pdf_path
            db.close()
            return True, "获取特定产品信息成功", result
        else:
            db.close()
            return False, "商品不存在", "null"

    except:
        return False, "连接数据库失败", "null"


def enter_pdf(name, productId, pdf_path):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        value = dict()
        value["pdf_path"] = pdf_path

        company_name = vendor_name2company_name(name)
        condition = dict()
        condition['company'] = company_name
        condition['commodity_id'] = productId

        # 生成SQL语句
        query = sql.update("provide", value, condition)

        # 使用execute方法执行SQL语句
        try:
            cursor.execute(query)
            db.commit()
            db.close()
            result = total_commoditys(company_name)
            return True, "录入pdf成功", result

        except:
            db.rollback()
            db.close()
            result = total_commoditys(company_name)
            return False, "录入pdf失败", result

    except:
        return False, "无法连接数据库" , "null"


def delete_product(name,productId):
    try:
        result = dict()
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        condition = dict()
        condition["commodity_id"] = productId
        condition["company"] = vendor_name2company_name(name)

        query = sql.delete("provide", condition)

        try:
            cursor.execute(query)
            db.commit()
            db.close()
            return True, "删除商品成功", "null"
        except:
            db.rollback()
            db.close()
            return False, "删除商品失败", "null"

    except:
        return False, "连接数据库失败", "null"


def get_price(company_name,commodity_id,spec):
    try:
        result = dict()
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        key = ["price"]

        condition = dict()
        condition["company"] = company_name
        condition["commodity_id"] = commodity_id
        condition["spec"] = spec

        query = sql.select("provide", key, condition, 0)
        if cursor.execute(query):
            data = cursor.fetchone()
            result['price'] = data[0]
            db.close()
            return True, "获取特定产品信息成功", result
        else:
            db.close()
            return False, "商品不存在", "null"

    except:
        return False, "获取价格失败", "null"


def get_spec(company_name,commodity_id):
    try:
        result = dict()
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        key = ["spec", "pdf_path"]

        condition = dict()
        condition["company"] = company_name
        condition["commodity_id"] = commodity_id

        query = sql.select("provide", key, condition, 0)
        print(query)

        if cursor.execute(query):
            data = cursor.fetchall()
            specs = []
            for row in data:
                specs.append(row[0])
            result['pdf_path'] = data[0][1]
            result['specs'] = specs
            db.close()
            return True, "获取支数和色卡成功", result
        else:
            db.close()
            return False, "商品不存在", "null"

    except:
        return False, "获取支数和色卡失败", "null"

