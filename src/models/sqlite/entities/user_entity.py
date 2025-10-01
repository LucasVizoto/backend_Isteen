from src.models.sqlite.settings.base import Base
from sqlalchemy import Column, String

class User(Base): 
    __tablename__ = 'users'

    id = Column(String, primary_key=True)

    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False, default='user')
    status = Column(String, nullable=False, default='active')

    def __repr__(self):
        return f"User [id={self.id}, username={self.username}, email={self.email}, role={self.role}, status={self.status}]"