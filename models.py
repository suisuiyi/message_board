# -*- coding: utf-8 -*-

"""
@author: peter.dai
@project: message_board
@file: models.py
@time: 2020/1/14 08:50
@desc:
"""
from datetime import datetime
from app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)

