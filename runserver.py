#coding:utf-8

import web


def load_urls():   
    urls_all = []
    from apps.main.urls import urls as urls
    urls_all += list(urls)
    return urls_all

urls = load_urls()
application = web.application(urls, autoreload=True)

if __name__ == '__main__':
    web.config.debug = True
    application.run()