#!/usr/bin/env python3
"""class LIFOCache that inherits from BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO-based caching system
    """
    def __init__(self):
        """Initalize cache
        """
        super().__init__()
        self.insertion_order = {}
        self.latest = 0

    def put(self, key, item):
        if all([key, item]):
            if len(self.cache_data) >= self.MAX_ITEMS and \
                    key not in self.cache_data:
                discard_key = self.get_last_in()
                self.cache_data.pop(discard_key)
                self.insertion_order.pop(discard_key)
                print('DISCARD: {}'.format(discard_key))
            self.cache_data[key] = item
            self.insertion_order[key] = self.latest
            self.latest += 1

    def get_last_in(self):
        for key, value in self.insertion_order.items():
            if value == self.latest - 1:
                return key
        return None

    def get(self, key):
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
