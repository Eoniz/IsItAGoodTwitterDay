from typing import List

from pydantic import BaseModel

from itagtd.infrastructure.entity.twitter.tweet import Tweet


class TrendTweets(BaseModel):
    trend: str = None
    tweets: List[Tweet] = None
