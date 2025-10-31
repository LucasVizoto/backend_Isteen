from abc import ABC, abstractmethod

from src.models.sqlite.entities.user_entity import User

class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        ...

    @abstractmethod
    def create_user(self, username: str, email: str, password_hash: str, role: str = 'user', status: str = 'active'):
        ...

    @abstractmethod
    def delete_user(self, user_id: int):
        ...

    @abstractmethod
    def update_user_status(self, user_id: int, status: str):
        ...

    @abstractmethod
    def update_user_data(self):
        ...