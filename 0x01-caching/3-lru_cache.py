#!/usr/bin/env python3
"""Defines a class LRUCache
"""


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A Least Recently Used (LRU) caching system
    """
    def __init__(self):
        """Initalize cache
        """
        super().__init__()
        self.age_bits = {}
        self.most_recently_used = 0

    def put(self, key, item):
        """Add item to cache
        """
        if all([key, item]):
            if len(self.cache_data) >= self.MAX_ITEMS and \
                    key not in self.cache_data:
                discard_key = self.get_lru()
                self.cache_data.pop(discard_key)
                self.age_bits.pop(discard_key)
                print('DISCARD: {}'.format(discard_key))
            self.cache_data[key] = item
            self.age_bits[key] = self.most_recently_used
            self.most_recently_used += 1
            print(self.age_bits)

    def get_lru(self):
        """Returns least recently used item in cache
        """
        lru_index = min(self.age_bits.values())
        for key, value in self.age_bits.items():
            if value == lru_index:
                return key
        return None

    def get(self, key):
        """Retrieve item from cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
