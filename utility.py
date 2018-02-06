# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"


def class_2_dict(obj):
    tmpdict = dict()
    tmpdict.update(obj.__dict__)
    return tmpdict


def dict_2_str(dictin):
    # seperate with ","
    tmplist = list()
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), str(v))
        tmplist.append(' ' + tmp + ' ')
    return ','.join(tmplist)


def dict_2_str_and(dictin):
    # seperate with "and"
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), str(v))
        tmplist.append(' ' + tmp + ' ')
    return ' and '.join(tmplist)


def path_2_base64(path):
    f = open(path)
    str64 = f.read()
    f.close()
    return str64


def base64_2_path(str64, id):
    path = "/root/textile_land/vendor_pic/"
    path += id
    path += "_pic.txt"
    f = open(path, 'w')
    f.write(str64)
    f.close()
    return path
