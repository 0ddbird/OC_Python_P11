from dataclasses import dataclass
from datetime import datetime


@dataclass
class Club:
    name: str
    points: int


class Competition:
    name: str
    date: datetime
    available_slots: int
