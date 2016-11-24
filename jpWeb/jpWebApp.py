# -*- coding:utf-8 -*-
# 2016-10-25 16:09
# auther:wjp
# 处理3个URL, GET /:首页，返回Home
# GET /signin: 登录页，显示登录表单
# POST /signin: 处理登录表单，显示登录结果

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
	return '<h1>Home</h1>'

@app.route('/signin', methods = ['GET'])
def signin_form():
	return '''<form action = "/signin" method = "post">
			  <p><input name = "username"></p>
			  <p><input type = "password" name = "password"></p>
			  <p><button type = "submit">Sign In</p>
			  </form>'''

@app.route('/signin', methods = ['POST'])
def signin():
	#需要从request对象读取表单内容：
	if request.form['username'] == 'admin' and request.form['password'] == 'password':
		return '<h3>你好, admin!</h3>'
	return '<h3>Bad username or password</h3>'


if __name__ == '__main__':
	app.run()