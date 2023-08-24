#!/usr/bin/env python3
"""class FIFOCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO-based caching system
    """
    def __init__(self):
        """Initalize cache
        """
        super().__init__()

    def put(self, key, item):
        if all([key, item]):
            if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
                discarded_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(discarded_key)
                print('DISCARD: {}'.format(discarded_key))
            self.cache_data[key] = item

    def get(self, key):
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None