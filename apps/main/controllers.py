#coding:utf-8

import views
from  web import form


class index:
    def GET(self):
        return views.Template("base").render() 
    
    

class login(object):
    def GET(self):
        fm = form.Form(
         form.Textbox("username", description="Username"),
        form.Textbox("email" , description="E-Mail"),
        form.Password("password", description="Password"),
        form.Password("password2", description="Repeat password"),
        form.Button("submit", type="submit", description="Register"),
        validators = [
            form.Validator("Passwords did't match", lambda i: i.password == i.password2)]
        )
        return fm.render()
        #return views.Template("login").render(name='1', password=23)