import json


class JSON:
    def __init__(self, base_url: str = "./data", file_name: str = None):
        self.file_path = f"{base_url}/{file_name}"
        self.__data: dict | None = {}
        self.load_data()

    def load_data(self) -> dict:
        with open(self.file_path, "r") as file:
            self.__data = json.load(file)
        return self.__data

    def get_data(self) -> dict:
        return self.__data
