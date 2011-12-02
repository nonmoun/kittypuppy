#coding:utf-8

import web
import controllers

urls = (
  "", controllers.index,
)

application = web.application(urls, locals())