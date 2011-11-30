#coding:utf-8

import web

urls = ('/.*', 'index')

class index:
    def GET(self):
        return "hello ,world"


application = web.application(urls, globals()).wsgifunc()