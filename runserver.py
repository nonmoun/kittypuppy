#coding:utf-8

import web
from apps.main.app import application as app_main
urls = (
    '/', app_main
)


if __name__ == '__main__':
    web.config.debug = True
    app = web.application(urls, globals())
    app.run()