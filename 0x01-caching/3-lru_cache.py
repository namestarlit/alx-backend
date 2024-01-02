#!/usr/bin/env python3
"""A module that implements a simple LRU caching algorithm"""
from collections import OrderedDict

try:
    BaseCaching = __import__("base_caching").BaseCaching
except ImportError as e:
    raise e(e.message)


class LRUCache(BaseCaching):
    """LRUCache class that implements the LRU cache algorithm"""

    def __init__(self):
        """Instantiates instances of LRUCache class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to the cache"""

        # Check if key or item is None
        if key is None or item is None:
            return None

        # Check if the cache is full, MAX_ITEMS reached
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the last in/least recently cache key-value pair from the cache
            removed_key, removed_value = self.cache_data.popitem(True)
            print("DISCARD: {}".format(removed_key))

        # Add the new item to the cache
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Get an item from the cache"""

        # Return the value if key exists, else None
        return self.cache_data.get(key, None)