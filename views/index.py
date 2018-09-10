'''
Created by zhousp on 18-9-9
'''

from tornado.web import RequestHandler

import os
import config

__author__ = 'zhousp'


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        url = self.reverse_url("other")
        self.write('<a href="%s">other</a>' % (url))


class HomeHandler(RequestHandler):
    # 该方法会在http方法之前调用
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        print(self.word1, self.word2)
        self.write("<h2>Home!</h2>")


class OtherHandler(RequestHandler):
    def initialize(self, word3, word4):
        self.word3 = word3
        self.word4 = word4

    def get(self, *args, **kwargs):
        print(self.word3, self.word4)
        self.write("<h2>Other!</h2>")


class HelloHandler(RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):
        print(h1 + "---" + h2 + "---" + h3)
        self.write("Hello, World!")


class Hello2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        # a = self.get_query_argument("a")
        # b = self.get_query_argument("b")
        # c = self.get_query_argument("c")
        # print(a, b, c)

        alist = self.get_query_arguments("a")
        print(alist[0], alist[1])
        self.write("Hello2!")


class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')

    def post(self, *args, **kwargs):
        name = self.get_body_argument("username")
        passwd = self.get_body_argument("passwd")
        hobbylist = self.get_body_arguments("hobby")
        print(name, passwd, hobbylist)
        self.write("sunck is a good boy!")


class ZhuyinHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.remote_ip)
        print(self.request.files)
        self.write("zhuyin is a good women")


class UpFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("upfile.html")

    def post(self, *args, **kwargs):
        files = self.request.files
        for file in files:
            fileArr = files[file]
            for fileObj in fileArr:
                # 存储路径
                filePath = os.path.join(config.BASE_DIR, 'upload/' + fileObj.filename)
                with open(filePath, 'wb') as f:
                    f.write(fileObj.body)

        self.write('ok')


class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hello")
        self.write("Hello1")
        self.write("Hello2")
        # 刷新缓冲区，关闭档次请求通道
        # 在finish下面不要write
        self.finish()


import json


class Json1Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "sunck",
            "age": 18,
            "height": 175,
            "weight": 60
        }
        jsonStr = json.dumps(per)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("sunck", "good")
        self.write(jsonStr)


class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "sunck",
            "age": 18,
            "height": 175,
            "weight": 60
        }
        self.write(per)


class HeaderHandler(RequestHandler):
    # 在进入http响应处理方法之前被调用，可以重写该方法来预先设置默认的headers
    def set_default_headers(self):
        self.set_header("Content-Type", "text/html; charset=UTF-8")

    def get(self, *args, **kwargs):
        pass


class StatusCodeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.set_status(404)

        # 自定义状态码
        self.set_status(999, "what's wrong?")
        self.write("************")


class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")


class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            code = 500
            self.write("500, 服务器内部错误")
        elif status_code == 404:
            code = 404
            self.write("404,资源不存在")
        self.set_status(code)

    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag == '0':
            self.send_error(500)

        self.write("you are right")
