from abc import ABC, abstractmethod
from backend.api.core.entities.user import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass