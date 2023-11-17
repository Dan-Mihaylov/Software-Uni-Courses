from sqlalchemy import (Column, Integer, Text, String, ForeignKey)
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)

    chef_id = Column(Integer, ForeignKey("chefs.id"))  # FK which coll does it access in the chefs table
    chef = relationship("Chef", back_populates="recipes")


class Chef(Base):
    __tablename__ = "chefs"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    recipes = relationship("Recipe", back_populates="chef")





