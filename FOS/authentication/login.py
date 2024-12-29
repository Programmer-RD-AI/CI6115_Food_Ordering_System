from ..repositories.authentication_repository import AuthenticationRepository
from ..models.user import User


class Login:
    def __init__(
        self,
        username: str,
        password: str,
        email: str,
        auth_repo: AuthenticationRepository,
    ) -> None:
        self.user = User(username, password, email)
        self.auth_repo = auth_repo

    def login(self) -> bool:
        exists_idx = self.auth_repo.check_if_user_exists(
            self.user.username, self.user.email
        )
        if exists_idx is None:
            return False
        _, username, email, password = self.auth_repo.get_user(exists_idx)
        if all(
            [
                any([username == self.user.get_username, email == self.user.get_email]),
                password == self.user.get_password,
            ]
        ):
            return True
        return False
