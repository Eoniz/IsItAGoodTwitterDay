import os
import time
import json
from typing import Any

from itagtd.infrastructure.configuration.configuration import get_configuration
from itagtd.infrastructure.json.itagtd_encoder import ITAGTDEncoder
from itagtd.infrastructure.value_object.cache.cache_item import CacheItem


def _get_data_from_file(cls, path: str) -> Any:
    with open(path) as json_file:
        return cls(json.load(json_file))


def cache(cls, expiration: float = 3600):
    __cache = {}

    def inner(func):
        def decorator(*args, **kwargs):
            __config = get_configuration()

            __items_to_remove = []
            for key, cache_item in __cache.items():
                if time.time() > cache_item.last_update + expiration:
                    __items_to_remove.append(cache_item)

            for item_to_remove in __items_to_remove:
                del __cache[item_to_remove.name]

                item_path = os.path.join(__config.project_root, f"cache/{item_to_remove.name}.json")
                if os.path.exists(item_path):
                    os.remove(item_path)

            if (
                    func.__qualname__ in __cache
                    and time.time() <= __cache[func.__qualname__].last_update + expiration
            ):
                return __cache[func.__qualname__].data

            path = os.path.join(__config.project_root, f"cache/{func.__qualname__}.json")

            if (
                    os.path.exists(path)
                    and time.time() <= os.path.getmtime(path) + expiration
            ):
                data = _get_data_from_file(cls=cls, path=path)
                __cache[func.__qualname__] = CacheItem(data=data, name=func.__qualname__)

                return data

            func_result = func(*args, **kwargs)
            with open(path, "w") as file:
                json.dump(func_result, file, indent=4, sort_keys=True, cls=ITAGTDEncoder)

            __cache[func.__qualname__] = CacheItem(data=func_result, name=func.__qualname__)

            return func_result
        return decorator
    return inner
