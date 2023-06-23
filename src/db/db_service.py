from src.db.base import Session, engine, Base
from src.db.user import User

# Create database tables based on the defined models
Base.metadata.create_all(engine)


# Function to add a user to the database
def add(user):
    """
    Add user into the database
    :param user:
    :return: None
    """
    session = Session()
    session.add(user)
    session.commit()
    session.close()


# Function to retrieve a user from the database based on login
def get_user(login):
    """
    Get user by login
    :param login:
    :return: user if exists or None
    """
    session = Session()
    users = session.query(User).filter(User.login == login).all()
    for user in users:
        if user.login == login:
            return user
    return None
