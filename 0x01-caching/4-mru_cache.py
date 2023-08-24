#!/usr/bin/env python3
"""Defines a class MRUCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A Most Recently Used (MRU) caching system
    """
    def __init__(self):
        """Initalize cache
        """
        super().__init__()
        self.recency = []

    def put(self, key, item):
        """Add item to cache
        """
        self.cache_data[key] = item
        if all([key, item]):
            if key not in self.recency:
                self.recency.append(key)
            else:
                self.recency.append(self.recency.pop(self.recency.index(key)))

            if len(self.recency) > self.MAX_ITEMS:
                discard_key = self.recency.pop(-2)
                self.cache_data.pop(discard_key)
                print('DISCARD: {}'.format(discard_key))

    def get(self, key):
        """Retrieve a cache item
        """
        if key and key in self.cache_data:
            self.recency.append(self.recency.pop(self.recency.index(key)))
            return self.cache_data.get(key)
        return None
