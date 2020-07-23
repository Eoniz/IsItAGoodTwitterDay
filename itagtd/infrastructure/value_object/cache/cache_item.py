import copy
import time
from typing import Any


class CacheItem:
    def __init__(
            self, *,
            name: str,
            last_update: float = None,
            data: Any = None,
    ):
        self._name = name
        self._last_update = last_update if last_update else time.time()
        self._data = data

    @property
    def name(self) -> str:
        return self._name

    @property
    def data(self) -> Any:
        """
        Read Only: copy of the Data saved
        :return: copy of the Data saved
        """
        return copy.deepcopy(self._data)

    @property
    def last_update(self) -> float:
        """
        Read Only: Last Update time in s.ms (time.time())
        :return: Last Update Time
        """
        return self._last_update
