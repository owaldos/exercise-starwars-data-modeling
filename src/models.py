import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    dob = Column(String(80), nullable=False)
    favorites = relationship('Favorite', backref='user', uselist=True)
  

    def login(self):
        return {
            "username": self.username,
            "password": self.password
        }

class Favorites(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    height = Column(Integer, nullable=False)
    hair_color= Column(String(20), nullable=False)
    eyes_color = Column(String(20), nullable=False)
    homeworld = Column(String(40), nullable = False)



class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    population= Column(Integer, nullable=False)
    terrain = Column(String(60), nullable=False)
    planet_name = Column(String(40), nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
