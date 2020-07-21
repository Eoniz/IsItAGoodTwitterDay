from pydantic import BaseModel

from itagtd.infrastructure.entity.configuration import TwitterSecrets


class Secrets(BaseModel):
    twitter: TwitterSecrets = None
