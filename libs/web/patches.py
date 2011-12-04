#coding:utf-8

import web
import urlparse

def set_context_params():
    method = web.ctx.method
    if not web.ctx.has_key(method):
        if method == "GET":
            params = urlparse.parse_qs(web.ctx.query, 1)
            for k in params:
                if len(params[k]) == 1:
                    params[k] = params[k][0]
        web.ctx[method] = params
    return web.ctx[method]
