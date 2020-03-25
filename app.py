# -*- coding: utf-8 -*-

"""
@author: peter.dai
@project: message_board
@file: app.py
@time: 2020/1/14 08:55
@desc:
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# 初始化 flask 程序实例

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv['SECRET_KEY', 'little_fox']

dev_db = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
# 初始化一个数据库实例
db = SQLAlchemy(app)
boostrap = Bootstrap(app)


if __name__ == '__main__':
    print(dev_db)
