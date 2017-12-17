# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"


class User:
    def __init__(self, username, number, password):
        self.username = username
        self.number = number
        self.password = password


class Response:
    def __init__(self, isSuccess, msg):
        self.isSuccess = isSuccess
        self.msg = msg


class Commodity:
    def __init__(self, name , category, price ):
        self.name = name
        self.category = category
        self.price = price

