from ..models.user import User
from ..repositories.authentication_repository import AuthenticationRepository


class Register:
    def __init__(
        self,
        username: str,
        password: str,
        email: str,
        auth_repo: AuthenticationRepository,
    ):
        self.user = User(username, password, email)
        self.auth_repo = auth_repo

    def register(self) -> None | User:
        if not self.auth_repo.check_if_user_exists(
            self.user.get_username, self.user.get_email
        ):
            self.auth_repo.add_user(
                self.user,
            )
            return self.user
        return
