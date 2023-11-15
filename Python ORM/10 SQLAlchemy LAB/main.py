from sqlalchemy import create_engine
from settings import DATABASE_URL
from sqlalchemy.orm import sessionmaker

# Pool size is valuable when many people are trying to use the DB at the same time
# This way you create DB connections that can be reused and shared to reduce DB hits by all users
# In this code we use a standard pool_size of 10 that can go up to 20 if needed for short
# Periods of time.
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Create the Session and bind it to the current db_engine
Session = sessionmaker(bind=engine)






