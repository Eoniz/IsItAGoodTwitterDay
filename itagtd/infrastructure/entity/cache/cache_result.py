import time
from typing import Any


class CacheResult:
    def __init__(self, value: Any = None):
        self.value: Any = value
        self.last_update = time.time()
