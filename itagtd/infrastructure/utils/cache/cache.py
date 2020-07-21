import os
import time
import json

from itagtd.infrastructure.configuration.configuration import get_configuration
from itagtd.infrastructure.json.itagtd_encoder import ITAGTDEncoder


def cache(cls, expiration: float = 3600):
    def inner(func):
        def decorator(*args, **kwargs):
            __config = get_configuration()
            path = os.path.join(__config.project_root, f"cache/{func.__qualname__}.json")

            if os.path.exists(path):
                if time.time() - expiration < os.path.getmtime(path):
                    with open(path) as json_file:
                        return cls(json.load(json_file))

            func_result = func(*args, **kwargs)
            with open(path, "w") as file:
                json.dump(func_result, file, indent=4, sort_keys=True, cls=ITAGTDEncoder)

            return func_result

        return decorator
    return inner
