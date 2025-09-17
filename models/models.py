
from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

engine = create_engine()

#Базовый класс
class Base(declarative_base): pass

#Таблица юзеров
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True,)
    name = Column(String,maxlen=20)
    surname = Column(String,maxlen=20)
    age = Column(Integer)
