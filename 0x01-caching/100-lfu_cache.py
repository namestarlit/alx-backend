#!/usr/bin/env python3
"""A module to implement a simple LFU caching algorithm"""
from collections import defaultdict, OrderedDict

try:
    BaseCaching = __import__("base_caching").BaseCaching
except ImportError as e:
    raise e(e.message)


class LFUCache(BaseCaching):
    """A LFUCache class that implements LFU Caching algorithm"""

    def __init__(self):
        """Instantiates an instance of LFUCache class"""
        super().__init__()

        # Store ordered key-value pair of cache data
        self.cache_data = OrderedDict()

        # Store the access frequency of each key in the cache
        self.key_frequency = defaultdict(int)
        self.min_frequency = 0

    def __evict_least_frequent(self):
        """Evict the least frequently used item from the cache"""
        min_frequency_keys = [
            key
            for key, freq in self.key_frequency.items()
            if freq == self.min_frequency
        ]

        if min_frequency_keys:
            # Remove the least frequently, and recently used cache
            key_to_remove = min_frequency_keys[0]
            self.cache_data.pop(key_to_remove, None)
            self.key_frequency.pop(key_to_remove, None)

            print("DISCARD: {}".format(key_to_remove))
        else:
            # Remove the least recently used cache
            key_to_remove, _ = self.cache_data.popitem(True)
            print("DISCARD: {}".format(key_to_remove))

    def put(self, key, item):
        """Adds an item to the cache"""

        # Check if the key or item is not provided
        if key is None or item is None:
            return None

        if key in self.cache_data:
            # Update existing item
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            # Check if max capacity is reached
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the least frequently used cache
                self.__evict_least_frequent()

            # Add new item
            self.cache_data[key] = item
            self.key_frequency[key] = 1
            self.min_frequency = 1

    def get(self, key):
        """Gets a cache with the specified key"""
        if key is not None and key in self.cache_data:
            # Increment frequency and move to the new frequency bucket
            self.key_frequency[key] += 1
            self.cache_data.move_to_end(key, last=False)
            self.min_frequency = min(
                self.min_frequency, self.key_frequency[key]
            )

        # Return the cache if key exists, else None
        return self.cache_data.get(key, None)
