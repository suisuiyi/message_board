import os
import sys
from flask import Flask, redirect, url_for, flash, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 设置密钥
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'little_fox')

db = SQLAlchemy(app)
# 配置数据库的地址：仅部署到unix系统上
# 确认是什么系统？
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
# 配置数据的地址
dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
"""
# 数据库相关设置
# 1.数据库地址URI
# 2.数据库更新
"""
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', dev_db)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
