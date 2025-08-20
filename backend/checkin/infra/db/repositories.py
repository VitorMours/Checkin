from checkin.core.interfaces.user_repository import UserRepositoryInterface
from checkin.core.entities.user import User as UserEntity
from checkin.infra.db.models import User
from typing import List

class UserRepository(UserRepositoryInterface):
    def get_all(self) -> List[UserEntity]:
        users = User.objects.all()
        return [
            UserEntity(
            id = user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password
        ) for user in users
        ]
    
    def create(self, user: User) -> User:
        new_user = User.objects.create(
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            password=user.password
        )
        new_user.set_password(user.password)
        new_user.save()
        return new_user