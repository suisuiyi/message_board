# -*- coding: utf-8 -*-

"""
@author: peter.dai
@project: message_board
@file: forms.py
@time: 2020/1/14 08:53
@desc:
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    sumbmit = SubmitField()

