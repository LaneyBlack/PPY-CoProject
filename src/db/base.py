from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://s24382:s24382@212.182.24.105:15432/s24382")
Session = sessionmaker(bind=engine)

Base = declarative_base()
