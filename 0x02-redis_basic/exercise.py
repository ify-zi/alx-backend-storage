#!/usr/bin/env python3
"""
    MOdule REDIS Basic
"""

import uuid
import random
import redis
from typing import Union, Optional, Callable


class Cache:
    """ cache class definiition"""

    def __init__(self):
        """definition function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        """store method declaration"""
        id_key = str(uuid.uuid4())
        self._redis.set(id_key, data)
        return id_key

    def get(self, key: str,
            fn: Optional[Callable]) -> Union[str, int, bytes, float]:
        """ return a data from a memor"""
        data = self._redis.get(key)
        if key is not None and fn is not None:
            data = fn(data)
        return data

    def get_int(self, data: Union[str, int, bytes, float]) -> Union[int, None]:
        """parametised the data to a format"""
        return self._redis.get(data)

    def get_str(self, data: Union[str, int, bytes, float]) -> Union[str, None]:
        """parametise the data to str format"""
        return self._redis.get(data)
