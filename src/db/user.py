from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL, TEXT
from src.db.base import Base
import base64


def password_encode(password):
    return base64.b64encode(password.encode("utf-8"))


def password_decode(code):
    return base64.b64decode(code).decode("utf-8")


class User(Base):
    __tablename__ = "user"

    login = Column(VARCHAR, primary_key=True)
    password = Column(VARCHAR)

    def __init__(self, login, password):
        self.login = login
        self.password = password
