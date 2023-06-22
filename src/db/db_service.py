from src.db.base import Session, engine, Base
from src.db.user import User

Base.metadata.create_all(engine)


def add(user):
    session = Session()
    session.add(user)
    session.commit()
    session.close()


def get_user(login):
    """

    :type login: string
    """
    session = Session()
    users = session.query(User).filter(User.login == login).all()
    for user in users:
        if user.login == login:
            return user
    return None
