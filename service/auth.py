from dataclasses import dataclass
from exception import UserNotFound, PasswordIncorrect
from models import UserProfile
from schema import UserLoginSchema
from repository.userrepository import UserRepository

@dataclass
class AuthService:
    user_repository: UserRepository
    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _validate_auth_user(user: UserProfile, password: str):
        if not user:
            raise UserNotFound
        if user.password != password:
            return PasswordIncorrect