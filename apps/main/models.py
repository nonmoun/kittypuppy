#coding:utf-8

from sqlalchemy import *
from utils.model import BaseModel, Session

class User(BaseModel):
    __table__ = "users"
    
    id = Column(Integer, primary_key=True)
    account = Column(String)
    password = Column(String)
    nickname = Column(String)
    email = Column(String)
    registered = Column(DateTime)
    group_id = Column(Integer)
    
    
class Post(BaseModel):
    __table__ = "posts"
    
    id = Column(Integer, primary_key=True)
    user_id =  Column(Integer)
    author = Column(String)
    created = Column(TIMESTAMP)
    modified = Column(DateTime)
    title = Column(String(100))
    content = Column(TEXT)
    status = Column(Integer)
    type_id = Column(Integer)
    tag_id = Column(Integer)
    