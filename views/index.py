'''
Created by zhousp on 18-9-9
'''

from tornado.web import RequestHandler

__author__ = 'zhousp'


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h2>Hello,Tornado!</h2>")


class HomeHandler(RequestHandler):

    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *args, **kwargs):
        print(self.word1, self.word2)
        self.write("<h2>Home!</h2>")
