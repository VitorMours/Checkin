from typing import List
from backend.api.core.interfaces.user_repository import UserRepositoryInterface
from backend.api.core.entities.user import User

class UserRepository(UserRepositoryInterface):
    def get_all(self) -> List[User]:
        pass
    
    def create(self, user: User) -> User:
        pass