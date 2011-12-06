#coding:utf-8

import views
from  web import form
import web

class index:
    def GET(self):
        return views.Template("base").render() 
    

class login:
    def GET(self):
        fm = form.Form(
            form.Textbox("username", description="Username"),
            form.Password("pas3swor2d", description="Pa23ssword"),
            form.Button("submit", type="submit", description="Register"),
            validators = [
                form.Validator("Passwords did't match", lambda i: i.password == i.password2)
                ]
            )
        return fm.render()
        #return views.Template("login").render(name='1', password=23)
      
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