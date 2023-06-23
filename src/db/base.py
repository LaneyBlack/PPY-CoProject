from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.settings import DB_STRING


# Create an engine using the database connection string
engine = create_engine(DB_STRING)
# Create a session factory using the engine
Session = sessionmaker(bind=engine)
# Create a declarative base class
Base = declarative_base()
