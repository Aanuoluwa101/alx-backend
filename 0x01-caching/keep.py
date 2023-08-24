#!/usr/bin/env python3
"""Defines a class LRUCache that inherits from BaseCaching and is a caching system
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
        self.oldest = 0

    def put(self, key, item):
        print("age_bits: ", self.age_bits)
        if all([key, item]):
            if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
                lru_age = min(list(self.age_bits.keys()))
                discarded_key = self.age_bits.pop(lru_age)

                self.cache_data.pop(discarded_key)
                print('DISCARD: {}'.format(discarded_key))
            self.cache_data[key] = item
            self.age_bits = {key: value for key, value in self.age_bits.items() if value != key}
            self.age_bits[self.oldest] = key
            self.oldest += 1

    def get(self, key):
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")


print(my_cache.age_bits)
# my_cache.print_cache()
# print(my_cache.get("B"))
my_cache.put("E", "Battery")
print(my_cache.age_bits)


# my_cache.print_cache()
my_cache.put("C", "Street")
print(my_cache.age_bits)

# my_cache.print_cache()
# print(my_cache.get("A"))
# print(my_cache.get("B"))
# print(my_cache.get("C"))
# my_cache.put("F", "Mission")
# my_cache.print_cache()
# my_cache.put("G", "San Francisco")
# my_cache.print_cache()
# my_cache.put("H", "H")
# my_cache.print_cache()
# my_cache.put("I", "I")
# my_cache.print_cache()
# my_cache.put("J", "J")
# my_cache.print_cache()
# my_cache.put("K", "K")
# my_cache.print_cache()
