#!/usr/bin/python3
from flask import Flask, render_template
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt

import entities
import sql
import utility
#jjjjjjjjjjjjjjjjj
app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'wujiahao.'
app.config['MYSQL_DB'] = 'flaskTest'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# CREATE TABLE users(id INT(20) AUTO_INCREMENT PRIMARY KEY , name VARCHAR(100), email VARCHAR(100) UNIQUE , username VARCHAR(45)  ,phone_number VARCHAR(20), password VARCHAR(100),register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

# Init MySQL
mysql = MySQL(app)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/register/')
def registerProcess():
    name = "zhangqi"
    email = "zhangq235@mail2.sysu.edu.cn"
    username = "Wink"
    password = "123456"
    phone_number = "18819253694"

    password = sha256_crypt.hash(password)

    password_verify = sha256_crypt.verify("123456", password)

    user = entities.User(name, username, phone_number, email, password)

    # Create cursor
    cur = mysql.connection.cursor()

    query = sql.insert('users', utility.class_2_dict(user))

    result = cur.execute(query)

    # Commit to DB
    mysql.connection.commit()

    # Close connection
    cur.close()

    if password_verify:
        return str(result)


@app.route('/userinfo/')
def userinfoProcess():
    # Create cursor
    cur = mysql.connection.cursor()

    tablename = "users"
    select_key = ["phone_number", "email"]

    condition = {}
    condition["username"] = "Jeako"

    query = sql.select(tablename, select_key, condition, 0)

    result = cur.execute(query)

    rs = cur.fetchall()

    # Commit to DB
    mysql.connection.commit()

    # Close connection
    cur.close()

    return str(rs)


@app.route('/updateuserinfo/')
def updateuserinfoProcess():
    # Create cursor
    cur = mysql.connection.cursor()

    tablename = "users"
    value = {}
    value["username"] = "Wink"
    condition = {}
    condition["name"] = "zhangqi"

    query = sql.update(tablename, value, condition)

    result = cur.execute(query)

    # Commit to DB
    mysql.connection.commit()

    # Close connection
    cur.close()

    if result:
        return "Success"
    else:
        return "Fail"


def main():
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()
