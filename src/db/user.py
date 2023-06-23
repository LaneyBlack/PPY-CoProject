"""
User Model and Password Encoding
"""

from sqlalchemy import Column, INTEGER, VARCHAR, DECIMAL, TEXT
from src.db.base import Base
import base64


def password_encode(password):
    """
    Encode a password using base64 encoding.
    :param password:str The password to encode.
    :return: str: The encoded password.
    """
    return base64.b64encode(password.encode("utf-8"))


def password_decode(code):
    """
    Decode a password using base64 encoding.
    :param code:str The string already encoded.
    :return: str: The decoded string.
    """
    return base64.b64decode(code).decode("utf-8")


class User(Base):
    """
    User Model for the 'user' table in the database.

    Attributes:
        __tablename__ (str): The name of the database table.
        login (Column): The login column of the user table.
        password (Column): The password column of the user table.
    """
    __tablename__ = "user"

    login = Column(VARCHAR, primary_key=True)
    password = Column(VARCHAR)

    def __init__(self, login, password):
        """
        Initialise a User object
        :param login:str:
        :param password:str:
        """
        self.login = login
        self.password = password
