# -*- coding: utf-8 -*-

"""
@author: peter.dai
@project: message_board
@file: models.py
@time: 2020/4/3 08:14
@desc:
"""
from app import db
from datetime import datetime
"""
创建一个留言板的模型类
1.数据库字段包含 id、name、message、timestamp

"""


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
