from json import JSONEncoder

from pydantic import BaseModel


class ITAGTDEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, BaseModel):
            return o.dict()

        return super().default(o)
