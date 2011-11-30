#coding:utf-8
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))

import web

urls = ('/.*', 'index')
s = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>网络媒体技术部</title>
    <script src="/static/js/jquery-1.7.1.min.js" type="text/javascript"></script>
</head>
<body>
<?php require_once 'inc/header.view.php'; ?>
<div class="main">
    <h1>B4网媒测试平台</h1>
</div>
<?php require_once 'inc/footer.view.php'; ?>
</body>
</html>
"""

class index:
    def GET(self):
        return s


application = web.application(urls, globals()).wsgifunc()
