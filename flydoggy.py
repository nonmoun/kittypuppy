#coding:utf-8
import sys
import os

current_path = os.path.dirname(__file__)
sys.path.append(current_path)
sys.path.append(os.path.join(current_path, "libs"))

import web
from runserver import application

application = application.wsgifunc()
