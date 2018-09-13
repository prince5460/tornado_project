'''
Created by ZhouSp 18-9-11.
'''

from tornado.web import RequestHandler
from models import Students

import os
import config

__author__ = 'zhou'


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        temp = 100
        per = {
            "name": "sunck",
            "age": 18,
        }
        flag = 0

        stus = [
            {
                "name": "lilei",
                "age": 18
            },
            {
                "name": "hanmeimei",
                "age": 16
            }
        ]
        '''
            <!--<h1>name : {{per["name"]}}</h1>-->
        '''
        # self.render("home.html", num=temp, per=per)
        '''
        <h1>name:{{name}}</h1>
        <h1>age:{{age}}</h1>
        '''
        self.render("home.html", num=temp, **per, flag=flag, stus=stus)


class FuncHandler(RequestHandler):
    def get(self, *args, **kwargs):
        def mySum(n1, n2):
            return n1 + n2

        self.render('func.html', mySum=mySum)


# 自动转义
class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1>sunck is a good man</h1>"
        self.render('trans.html', str=str)


class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('cart.html')


class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):

        # 插入数据
        # stu = Students("liudehua",18)
        # stu.save()
        # self.write("ok")

        # 从数据库中提取数据
        stus = Students.all()
        self.render('students.html', stus=stus)
