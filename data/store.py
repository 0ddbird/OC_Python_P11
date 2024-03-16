import json
import os
from enum import Enum

from config import DB_PATH


class Models(Enum):
    CLUB = "Club"
    COMPETITION = "Competition"


class ObjectDoesNotExist(Exception):
    pass


class Store:
    model_name: str
    objects: list[dict]

    def __init__(self, model_name: str):
        self.model_name = model_name

    def save(self) -> None:
        path = os.path.join(DB_PATH, f"{self.model_name.lower()}s.json")
        with open(path, "w") as file:
            json.dump({f"{self.model_name.lower()}s": self.objects}, file, indent=4)

    def load(self) -> None:
        path = os.path.join(DB_PATH, f"{self.model_name.lower()}s.json")
        with open(path, "r") as file:
            self.objects = json.load(file)[self.model_name.lower() + "s"]

    def get(self, attr: str, val: str) -> dict:
        for obj in self.objects:
            if obj[attr] == val:
                return obj
        raise ObjectDoesNotExist(f"{self.model_name} not found for {attr}: {val}")

    def get_all(self):
        return self.objects


class ClubStore(Store):
    def __init__(self):
        super().__init__(Models.CLUB.value)


class CompetitionStore(Store):
    def __init__(self):
        super().__init__(Models.COMPETITION.value)


ClubStore = ClubStore()
ClubStore.load()

CompetitionStore = CompetitionStore()
CompetitionStore.load()

