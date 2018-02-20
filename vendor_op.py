# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql
import utility
from db_link import commodity_id2commodity_name
from product_op import total_commoditys


def vendor_exist(name_get):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 查询字段
        key = ['company_name']

        # 查询条件
        condition = dict()
        condition['username'] = name_get

        # 生成SQL语句
        query = sql.select("vendor", key, condition, 0)
        # 使用execute方法执行SQL语句
        if cursor.execute(query):
            # 获取结果
            data = cursor.fetchone()

            result = dict()
            if data[0]:
                result['new'] = False
                # 关闭数据库连接
                db.close()
                return True, "查询是否是新商家成功", result
            else:
                result['new'] = True
                # 关闭数据库连接
                db.close()
                return True, "查询是否是新商家成功", result


        else:

            # 关闭数据库连接
            db.close()
            return False, "查询是否是新商家失败", "null"


    except:
        return False, "无法连接数据库" , "null"


def vendor_info(name_get):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 查询字段
        key = ['company_name', 'company_address', 'company_number', 'company_tax', 'main_product', 'company_pic']

        # 查询条件
        condition = dict()
        condition['username'] = name_get

        # 生成SQL语句
        query = sql.select("vendor", key, condition, 0)
        print(query)
        # 使用execute方法执行SQL语句
        if cursor.execute(query):
            # 获取结果
            data = cursor.fetchone()

            result = dict()
            result['company'] = data[0]
            result['address'] = data[1]
            result['phone'] = data[2]
            result['fax'] = data[3]
            result['star'] = commodity_id2commodity_name(data[4])
            try:
                result['pic'] = utility.path_2_base64(data[5])
            except:
                result['pic'] = "null"

            return True, "获取商家基本信息成功", result

        else:

            # 关闭数据库连接
            db.close()
            return False, "获取商家基本信息成功失败", "null"

    except:
        return False, "无法连接数据库" , "null"


def vendor_edit(name_get, basicinfo):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest", charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()


        # 查询字段
        value = dict()
        value['company_name'] = basicinfo.company
        value['company_address'] = basicinfo.address
        value['company_number'] = basicinfo.phone
        value['company_tax'] = basicinfo.fax
        value['main_product'] = basicinfo.star
        value['company_pic'] = utility.base64_2_path(basicinfo.pic, name_get)

        # 查询条件
        condition = dict()
        condition['username'] = name_get

        # 生成SQL语句
        query = sql.update("vendor", value, condition)
        # 使用execute方法执行SQL语句
        try:
            cursor.execute(query)
            db.commit()

        except:
            db.rollback()
            db.close()
            return False, "录入商家信息失败"

        db.close()
        return True, "录入商家信息成功"

    except:
        return False, "无法连接数据库" , "null"


def vendor_total_info(name_get):
    try:
        vi = vendor_info(name_get)
        if vi[0]:
            # 获取结果
            result = vi[2]
            result['products'] = total_commoditys(result["company"])
            try:
                result['pic'] = utility.path_2_base64(result["pic"])
            except:
                result['pic'] = "null"
            return True, "获取商家基本信息成功", result

        else:
            return False, "获取商家基本信息成功失败", "null"

    except:
        return False, "无法连接数据库" , "null"
