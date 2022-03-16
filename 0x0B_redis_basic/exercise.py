#!/usr/bin/env python3
""" Redis basic
"""
import redis
import uuid
from typing import Union, Optional, Callable
import sys


class Cache(object):
    """ Cache class
    """
    def __init__(self):
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ return a string"""
        key = str(uuid.uuid4())
        self.__redis[key] = data
        return key

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """ Take a key string argument and an optional Callable
        """
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_str(self, b: bytes) -> str:
        """ get str
        """
        return b.decode('utf-8')

    def get_int(self, b: bytes) -> int:
        """ get int
        """
        return int.from_bytes(b, sys.byteorder)
