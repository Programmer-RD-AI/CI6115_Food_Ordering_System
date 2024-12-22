import json
from typing import Self


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

    def set_data(self, new_data: dict) -> None:
        self.__data = new_data
        self.write_data()

    def add_data(self, key: str, value: any, assign=True, append=False) -> Self:
        if append:
            self.__data[key].append(value)
        else:
            self.__data[key] = value
        self.write_data()
        return self

    def write_data(self) -> None:
        with open(self.file_path, "w") as file:
            json.dump(self.__data, file, indent=4)
