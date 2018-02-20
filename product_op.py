# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql
import json
import utility
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
        result = list()
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
      
        key = ["id", "name"]
        condition = dict()

        query = sql.select("commodity", key, condition , 0)

        cursor.execute(query)

        commodities = cursor.fetchall()

        key = ["spec", "price", "pdf_path"]
        condition["company"] = company_name
        for commodity in commodities:
            per_commodity = dict()
            
            detail = list()

            condition["commodity_id"] = commodity[0]
            query = sql.select("provide", key, condition, 0)
            if cursor.execute(query):
                details = cursor.fetchall()
                for sp in details:
                    per_sp = dict()
                    per_sp["spec"] = sp[0]
                    per_sp["price"] = sp[1]
                    detail.append(per_sp)
                per_commodity["detail"] = detail
                per_commodity["productId"] = commodity[0]
                per_commodity["productName"] = commodity[1]
                per_commodity["pdf"] = details[0][2]
                result.append(per_commodity)
        db.close()
        return result


    except:
        return False, "获取商家详细信息失败", "null"
