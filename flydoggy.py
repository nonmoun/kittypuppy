#coding:utf-8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))

import web

urls = ('/.*', 'index')

class index:
    def GET(self):
        return "hello ,world"


application = web.application(urls, globals()).wsgifunc()
