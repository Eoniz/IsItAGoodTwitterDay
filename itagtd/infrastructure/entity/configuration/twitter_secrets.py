from pydantic import BaseModel


class TwitterSecrets(BaseModel):
    consumer_key: str = None
    consumer_secret: str = None
    access_key: str = None
    access_secret: str = None
    bearer: str = None
