from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from src.settings import DB_STRING

engine = create_engine(DB_STRING)
Session = sessionmaker(bind=engine)

Base = declarative_base()
