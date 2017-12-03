import utility


def insert(table, dict):
    # '''
    # create insert
    # @table tablename
    # @dict{}
    # '''
    sql = 'INSERT INTO %s SET ' % table
    sql += utility.dict_2_str(dict)
    return sql


def select(table, keys, conditions, isdistinct=0):
    # '''
    # create select
    # @table tablename str
    # @key what you want to select[]
    # @conditions {}
    # @isdistinct   int  wether repeat
    # '''
    if isdistinct:
        sql = 'select distinct %s ' % ",".join(keys)
    else:
        sql = 'select  %s ' % ",".join(keys)
    sql += ' from %s ' % table
    if conditions:
        sql += ' where %s ' % utility.dict_2_str_and(conditions)
    return sql


def update(table, value, conditions):
    #    create update
    # @table tablename
    # @value,dict {}
    # @conditions {}
    sql = 'update %s set ' % table
    sql += utility.dict_2_str(value)
    if conditions:
        sql += ' where %s ' % utility.dict_2_str_and(conditions)
    return sql


def delete(table, conditions):
    # '''
    # create delete tablename
    #
    # @conditions {}
    # '''
    sql = 'delete from  %s  ' % table
    if conditions:
        sql += ' where %s ' % utility.dict_2_str_and(conditions)
    return sql
