import utility
import sql
import MySQLdb


def register_process(user):
    try:
        # 打开数据库连接
        db = MySQLdb.connect("localhost", "root", "wujiahao.", "flaskTest")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 生成SQL语句
        query = sql.insert('users', utility.class_2_dict(user))

        # 使用execute方法执行SQL语句
        try:
            cursor.execute(query)

            db.commit()
        except:

            db.rollback()
            return "User already exist"

        # 关闭数据库连接
        db.close()

        return "Successfully Register"

    except:
        return "Unable to connect to DB"

