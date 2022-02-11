#!/usr/bin/python3
"""Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """Must return the value in self.cache_data"""
        if key is None:
            return None
        return self.cache_data.get(key)
