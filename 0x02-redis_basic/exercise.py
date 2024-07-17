#!/usr/bin/env python3
"""
    MOdule REDIS Basic
"""

import uuid
import random
import redis
from typing import Union


class Cache:
    """ cache class definiition"""

    def __init__(self):
        """definition function"""
        self._redis = redis.Redis()
        self._redis.flushdb()
        return

    def store(self, data: Union[str, bytes, float, int]) -> str:
        """store method declaration"""
        id_key = str(uuid.uuid4())
        self._redis.set(id_key, data)
        return id_key
