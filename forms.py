# -*- coding: utf-8 -*-

"""
@author: peter.dai
@project: message_board
@file: forms.py
@time: 2020/4/3 08:39
@desc:
"""
"""
创建表单类使用 flask_wtf框架里面的FlaskForm类
wtforms用于提供UI控件
wtforms.validators,用于提供校验空间

"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
