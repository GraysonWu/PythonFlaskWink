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


class Commodity:
    def __init__(self, name , category, price ):
        self.name = name
        self.category = category
        self.price = price

