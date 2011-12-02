#coding:utf-8
import sys
import os

current_path = os.path.dirname(__file__)
sys.path.append(current_path)
sys.path.append(os.path.join(current_path, "libs"))

import web
from app_main.app import application as app_main
urls = (
    '/', app_main
)

application = web.application(urls, globals()).wsgifunc()
