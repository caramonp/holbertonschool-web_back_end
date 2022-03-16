#!/usr/bin/env python3
""" Redis basic
"""
import redis
import uuid
from typing import Union, Optional, Callable
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls
    """
    key = method.__qualname__

    @wraps(method)
    def counter_wrapper(self, *args, **kwargs):
        """ Wrapper
        """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return counter_wrapper


def call_history(method: Callable) -> Callable:
    """ Store history
    """
    input_list_key = method.__qualname__ + ":inputs"
    output_list_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def set_history(self, *args, **kwargs):
        """ Set history
        """
        self._redis.rpush(input_list_key, str(args))
        res = method(self, *args, **kwargs)
        self._redis.rpush(output_list_key, str(res))
        return res

    return set_history


def replay(method: Callable) -> None:
    """ replay function to display the history of calls
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    in_list = redis.lrange(inputs, 0, -1)
    out_list = redis.lrange(outputs, 0, -1)
    redis_zipped = list(zip(in_list, out_list))
    for a, b in redis_zipped:
        attr, result = a.decode("utf-8"), b.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")


class Cache(object):
    """ Cache class
    """
    def __init__(self):
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    @call_history
    @count_calls
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
