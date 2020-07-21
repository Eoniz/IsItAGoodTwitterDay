import os
import time
import json

from itagtd.infrastructure.configuration.configuration import get_configuration
from itagtd.infrastructure.entity.cache.cache_result import CacheResult
from itagtd.infrastructure.json.itagtd_encoder import ITAGTDEncoder


def cache(expiration: float = 3600):
    __cache = {}

    def inner(func):
        def decorator(*args, **kwargs):
            __config = get_configuration()
            path = os.path.join(__config.project_root, f"cache/{func.__qualname__}.json")

            if func.__qualname__ in __cache:
                __cached_value = __cache[func.__qualname__]
                if time.time() - expiration < __cached_value.last_update:
                    return __cached_value.value
            if not os.path.exists(path):
                ...

            func_result = func(*args, **kwargs)
            with open(path, "w") as file:
                json.dump(func_result, file, indent=4, sort_keys=True, cls=ITAGTDEncoder)

            __cache[func.__qualname__] = CacheResult(value=func_result)

            return func_result

        return decorator
    return inner
