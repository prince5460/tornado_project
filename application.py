'''
Created by zhousp on 18-9-9
'''

import tornado.web
from views import index
import config

__author__ = 'zhousp'


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", index.IndexHandler),

            # 传参数
            (r"/home", index.HomeHandler, {"word1": "hello", "word2": "hi"}),
        ]

        super(Application, self).__init__(handlers, **config.settings)
