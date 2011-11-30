#coding:utf-8

import web
import views

urls = (
  "", views.index,
)

application = web.application(urls, locals())