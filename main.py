#!/usr/bin/python3
from flask import Flask, render_template
from passlib.hash import sha256_crypt

import entities
import sql
from register_process import register_process

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/register/')
def registerProcess():
    #TODO: set User with request

    #temp user
    name = "wujiahao"
    email = "wjh951022@gmail.com"
    password = "123456"
    phone_number = "13609756780"

    password = sha256_crypt.hash(password)

    password_verify = sha256_crypt.verify("123456", password)

    user = entities.User(name, phone_number, email, password)

    if password_verify:
        return register_process(user)


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


# CREATE TABLE users(id INT(20) AUTO_INCREMENT PRIMARY KEY , name VARCHAR(100)  UNIQUE, email VARCHAR(100) UNIQUE ,phone_number VARCHAR(20)  UNIQUE, password VARCHAR(100),register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

