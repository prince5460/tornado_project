'''
Created by zhousp on 18-9-9
'''

import tornado.web
from views import index, index2
import config
import os

__author__ = 'zhousp'


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r"/", index.IndexHandler),

            # 传参数
            (r"/home", index.HomeHandler, {"word1": "hello", "word2": "hi"}),

            # 反向解析
            tornado.web.url(r"/other", index.OtherHandler, {"word3": "hello2", "word4": "hi2"}, name='other'),

            # 提取uri特定部分
            # (r"/hello/(\w+)/(\w+)/(\w+)", index.HelloHandler),

            (r"/hello/(?P<h1>\w+)/(?P<h3>\w+)/(?P<h2>\w+)", index.HelloHandler),

            # get请求
            (r'/hello2', index.Hello2Handler),

            # post请求
            (r"/postfile", index.PostFileHandler),

            # request对象
            (r"/zhuyin", index.ZhuyinHandler),

            # 上传
            (r"/upfile", index.UpFileHandler),

            # write
            (r'/write', index.WriteHandler),

            # json
            (r"/json1", index.Json1Handler),
            (r"/json2", index.Json2Handler),

            # header
            (r"/header", index.HeaderHandler),

            # status code
            (r"/status", index.StatusCodeHandler),

            # 重定向
            (r'/index', index.RedirectHandler),

            # 错误处理
            (r'/iserror', index.ErrorHandler),

            # 渲染
            (r'/home2', index2.HomeHandler),

            # 函数
            (r'/func', index2.FuncHandler),

            # 转义
            (r'/trans', index2.TransHandler),

            # 继承
            (r'/cart', index2.CartHandler),

            # StaticFileHandler
            (r'/(.*)$', tornado.web.StaticFileHandler, {"path": os.path.join(config.BASE_DIR, "static/html"),
             "default_filename": "index.html"})

        ]

        super(Application, self).__init__(handlers, **config.settings)
