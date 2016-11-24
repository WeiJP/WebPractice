# -*- coding:utf-8 -*-
# 2016-10-26 10:09
# auther:wjp
# MVC模式，处理3个URL, GET /:首页，返回Home
# GET /signin: 登录页，显示登录表单
# POST /signin: 处理登录表单，显示登录结果

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/<name>', methods = ['GET', 'POST'])
def home(name):
	return render_template('home.html', name = name)

@app.route('/signin', methods = ['GET'])
def signin_form():
	return render_template('form.html', message = 'admin')

@app.route('/signin', methods = ['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username == 'admin' and password == 'password':
		return render_template('signin-ok.html')
	return render_template('form.html', message = '帐号和密码不符', username = username)

if __name__ == '__main__':
	app.run()


