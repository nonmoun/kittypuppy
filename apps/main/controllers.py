#coding:utf-8

import views
from  web import form
import web

class index:
    def GET(self):
        return views.Template("base").render() 
    
class login:
    def GET(self):
        return views.Template("login").render()
      
class register:
    def GET(self):
        return views.Template("register").render()
    
    def POST(self):
        return views.Template("register").render()

class editor:
    def GET(self):
        return views.Template("editor").render(content=a)
    
    def POST(self):

        a = web.input().idc
        return views.Template("editor").render(content=a)