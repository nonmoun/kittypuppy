#coding:utf-8

import os
from mako.lookup import TemplateLookup as _MakoTemplateLookup



_FACTORY = _MakoTemplateLookup(directories=[os.path.dirname(__file__)],
                                        input_encoding="utf-8",
                                        output_encoding="utf-8",)


def Template(uri):
    if not uri.endswith(".html"):
        uri = uri + ".html"
    return _FACTORY.get_template(uri)