def class_2_dict(obj):
    dict = {}
    dict.update(obj.__dict__)
    return dict


def dict_2_str(dictin):
    # seperate with ","
    tmplist = []
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
