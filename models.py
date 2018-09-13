'''
Created by zhousp on 18-9-13
'''

from orm.orm import ORM

__author__ = 'zhousp'


class Students(ORM):
    def __init__(self, name, age):
        self.name = name
        self.age = age
