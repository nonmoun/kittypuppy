import sys
import os


_current_dir = os.path.dirname(__file__)
def current_dir(path):
    return os.path.join(_current_dir, path)


sys.path.append(current_dir("libs"))


from pyramid.paster import get_app


app = get_app(current_dir("production.ini"), "main")
