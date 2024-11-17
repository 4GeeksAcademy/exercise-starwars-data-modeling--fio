import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base): 
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)  
    name = Column(String(200), nullable=False)
    population = Column(Integer)
    description = Column(String(250))  
    weather = Column(String(50), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=True)

class Favorite(Base):  
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')

    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    character = relationship('Character')

    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    planet = relationship('Planet')


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
