#coding:utf-8

import views


class index:
    def GET(self):
        return views.Template("base").render() 