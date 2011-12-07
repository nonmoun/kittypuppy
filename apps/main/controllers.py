#coding:utf-8

import views
from  web import form
import web

class index:
    def GET(self):
        return views.Template("base").render() 
    
class login:
    def GET(self):
        params = web.cookies()
        uid = params.get("uid", None)
        if uid and uid=="3333":
            return web.seeother("/")
        return views.Template("login").render()
    
    def POST(self):
        params = web.input()
        if "u" in params and "p" in params:
            web.setcookie("uid", "3333")
            return web.seeother("/")
        #
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