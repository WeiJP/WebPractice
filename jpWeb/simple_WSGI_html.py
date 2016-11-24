# -*- coding:utf-8 -*-
# 2016-10-25 15:44
# auther:wjp
# 实现Web应用程序的WSGI处理函数

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'Web')