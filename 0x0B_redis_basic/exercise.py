#!/usr/bin/env python3
""" Redis basic
"""
import redis
import uuid
from typing import Union

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
