import os
import sys
from flask import Flask, redirect, url_for, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from models import Message
from forms import MessageForm

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

# 编写视图函数，先写提交表单，底部的渲染效果有html文件来实现。
# 写好表单后，构建数据库实例，将数据持久化到DB
# 打印提示信息后
# 然后再次重定向到index页面。

# 渲染已有数据
# 1. 先查询出符合条件的数据
# 2. 使用将数据传递给html前端来渲染。


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash("表单已提交")
        return redirect(url_for('index'))
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
