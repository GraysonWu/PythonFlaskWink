# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"


class User:
    def __init__(self, username, number, password):
        self.username = username
        self.number = number
        self.password = password


class ResponseClass:
    def __init__(self, isSuccess, msg, data):
        self.isSuccess = isSuccess
        self.msg = msg
        self.data = data


class Basicinfo:
    def __init__(self, company, address, phone, fax, star, pic):
        self.company = company
        self.address = address
        self.phone = phone
        self.fax = fax
        self.star = star
        self.pic = pic