from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from main import engine


Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'))   # The ForeignKey specifies which column does this one reference
    user = relationship('User')

# Comment this because we are going to be using alembic to migrate table content and deal with the metadata
# Base.metadata.create_all(engine)

# Generate migration files with alembic using(  alembic revision --autogenerate -m "Add User Table"    )
# Update the db with (    alembic upgrade head    )



