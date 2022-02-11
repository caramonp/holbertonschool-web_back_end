#!/usr/bin/python3
"""Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic dictionary"""

    def put(self, key, item):
        """assign to the dictionary self.cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
        