#!/usr/bin/env python3
"""A module that implements a simple FIFO caching algorithm"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class that implements the FIFO cache algorithm"""

    def __init__(self):
        """Instantiates instances of FIFOCache class"""
        super().__init__()

    def put(self, key, item):
        """Adds an item to the cache"""

        # Check if key or item is None
        if key is None or item is None:
            return None

        # Check if the cache is full, MAX_ITEMS reached
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the key of the first added item from the cache
            first_key = next(iter(self.cache_data))

            # Remove the first in cache key-value pair from the cache
            self.cache_data.pop(first_key)
            print("DISCARD: {}".format(first_key))

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""

        # Check if the key is None
        if key is None:
            return None

        # Return the value if key exists, else None
        return self.cache_data.get(key, None)
