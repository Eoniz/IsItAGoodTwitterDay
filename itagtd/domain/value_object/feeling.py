from enum import Enum

from dataclasses import dataclass


@dataclass
class Feeling(str, Enum):
    happy: str = "happy"
    neutral: str = "neutral"
    unhappy: str = "unhappy"
