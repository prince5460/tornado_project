'''
Created by zhousp on 18-9-9
'''

import os

BASE_DIR = os.path.dirname(__file__)

__author__ = 'zhousp'

# 参数
options = {
    "port": 8000,
}

# 配置
settings = {
    "static_path": os.path.join(BASE_DIR, 'static'),
    "template_path": os.path.join(BASE_DIR, 'templates'),
    # 取消缓存编译的模板，取消缓存静态文件的hash值，提供追踪信息
    "debug": True,
    # 仅自动重启
    # "autoreload":True,
    # 关闭当前项目自动转义
    # "autoescape":None,
}
