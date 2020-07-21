from typing import Any

from pydantic import BaseModel


class Trend(BaseModel):
    name: str = None
    url: str = None
    promoted_content: Any = None
    query: str = None
    tweet_volume: int = None
