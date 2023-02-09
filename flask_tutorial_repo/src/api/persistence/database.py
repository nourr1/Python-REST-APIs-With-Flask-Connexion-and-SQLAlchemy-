from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "sqlite:///src/people.db"

# Creating an engine using the database url
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Defining a session Class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Instantiating a new session object
session = SessionLocal()


# Instantiating a 'Base' object from which the rest of classes shall inherit
Base = declarative_base()
