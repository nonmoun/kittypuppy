#coding:utf-8

import web




def load_urls():   
    urls_all = []
    from apps.main.urls import urls as urls
    urls_all += list(urls)
    return urls_all

urls = load_urls()
applicatoin = web.application(urls)


def my_processor(handler): 
    print 'before handling'
    
    result = handler() 
    print result
    print 'after handling'
    return result

applicatoin.add_processor(my_processor)

if __name__ == '__main__':
    web.config.debug = True
    applicatoin.run()