from pydantic import BaseModel
from tweepy import Status


class Tweet(BaseModel):
    favorite_count: int = None
    lang: str = None
    retweet_count: int = None
    text: str = None

    @classmethod
    def from_status(cls, status: Status):
        return Tweet(
            favorite_count=status.favorite_count,
            lang=status.lang,
            reteet_count=status.retweet_count,
            text=status.full_text
        )
