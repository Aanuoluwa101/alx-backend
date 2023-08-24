#!/usr/bin/env python3
""" Defines a caching system BasicCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ A caching system that extends BaseCaching
    """
    def __init__(self):
        """Initalize cache
        """
        super().__init__()

    def put(self, key, item):
        """Add item to cache
        """
        if all([key, item]):
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
