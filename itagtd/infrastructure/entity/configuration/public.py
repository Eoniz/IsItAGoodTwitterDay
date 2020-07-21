from pydantic import BaseModel

from itagtd.infrastructure.entity.configuration import TwitterPublic


class Public(BaseModel):
    twitter: TwitterPublic = None
