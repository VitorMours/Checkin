from abc import ABC, abstractmethod
from checkin.core.entities.user import User

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass