# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql
import json
import utility
from db_link import commodity_id2commodity_name, vendor_name2company_name


def enter_spec(enter_info):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        company_name = vendor_name2company_name(enter_info["name"])
        # 查询条件
        condition = dict()
        condition['company'] = company_name
        condition['commodity_id'] = enter_info["productId"]

        # 生成SQL语句
        query = sql.delete("provide", condition)

        # 使用execute方法执行SQL语句
        try:
            cursor.execute(query)
            db.commit()
            obj_list = enter_info["detail"]["arr"]
            print(type(obj_list))
            for obj in obj_list:
                condition = dict()
                condition["spec"] = obj["spec"]
                condition["price"] = obj["price"]
                condition["commodity_id"] = enter_info["productId"]
                condition["pdf_path"] = enter_info["url"]
                condition["company"] = company_name
                query = sql.insert("provide", condition)
                print(query)
                cursor.execute(query)
            db.commit()

        except:
            db.rollback()
            return False, "录入商品支数和价格失败", "null"

        db.close()
        return True, "录入商品支数和价格成功", "null"

    except:
        return False, "无法连接数据库" , "null"

