#coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings

engine = create_engine(settings.database)
Session = sessionmaker(engine)
BaseModel = declarative_base()