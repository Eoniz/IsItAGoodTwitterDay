from typing import List

from pydantic import BaseModel

from itagtd.domain.value_object.feeling import Feeling


class TrendsFeeling(BaseModel):
    trend: str = None
    feeling: Feeling = None
    polarities: List[float] = None
    tweets: List[str] = None
