from backend.api.core.entities.user import User 
from backend.api.core.interfaces.user_repository import UserRepositoryInterface


class CreateUser:
    def __init__(self, repository: UserRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, first_name: str, last_name: str, email: str, password: str) -> User:
        new_user = User(first_name=first_name, last_name=last_name, email=email, password = password)
        return self.repository.create(new_user)