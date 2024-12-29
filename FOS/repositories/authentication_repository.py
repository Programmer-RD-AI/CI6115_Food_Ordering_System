from ..utils.json_handler import JSON
from ..models.user import User


class AuthenticationRepository(object):
    def __init__(self, file_name: str = "users.json") -> None:
        self.json_instance = JSON(file_name=file_name)
        self.data = self.json_instance.get_data()

    def check_if_user_exists(self, username, email):
        for idx, user_id in enumerate(self.data["user_ids"]):
            if (
                self.data["usernames"][idx] == username
                or self.data["emails"][idx] == email
            ):
                return idx
        return None

    def get_user(self, idx: int) -> bool:
        return (
            self.data["user_ids"][idx],
            self.data["usernames"][idx],
            self.data["emails"][idx],
            self.data["passwords"][idx],
        )

    def add_user(self, user: User) -> bool:
        if self.check_if_user_exists(user.get_username, user.get_email):
            return False
        self.json_instance.add_data(
            "usernames", user.get_username, assign=False, append=True
        ).add_data("emails", user.get_email, assign=False, append=True).add_data(
            "passwords", user.get_password, assign=False, append=True
        ).add_data("user_ids", user.get_user_id, assign=False, append=True)
        return True
