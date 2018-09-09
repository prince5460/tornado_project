'''
Created by zhousp on 18-9-9
'''
import tornado.ioloop
import tornado.httpserver

from application import Application
import config

__author__ = 'zhousp'

if __name__ == '__main__':
    app = Application()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(config.options['port'])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
