# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: interfaceTest1
# author: "Lei Yong" 
# creation time: 2018/3/19 0019 23:19
# Email: leiyong711@163.com

import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()


def createTable():
    c.execute('CREATE TABLE user_info(id INTEGER PRIMARY KEY,'
              'name text NOT NULL UNIQUE ,password text NOT NULL )')
    conn.commit()
    conn.close()


def inset():
    c.execute("INSERT INTO user_info VALUES (? , ?, ?)", (None, 'leiyong2', '123'))
    conn.commit()
    conn.close()


def select():
    ca = []
    data = c.execute('SELECT * from user_info')
    for i in data:
        ca.append(i)
    return ca

#createTable()
#inset()
print select()

