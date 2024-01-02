#!/usr/bin/env python3
"""BaseCaching module"""


class BaseCaching:
    """A BaseCaching class defining:
    - Constants of a caching system
    - where the data is stored (a dictionary)

    """

    # Define the maximum number of items to store in cache
    MAX_ITEMS = 4

    def __init__(self):
        """Initializes an instance of BaseCaching class"""
        self.cache_data = {}

    def print_cache(self):
        """Prints the cache data"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        raise NotImplementedError(
            "put must be implemented in your cache class"
        )

    def get(self, key):
        """Get an item by key"""
        raise NotImplementedError(
            "get must be implemented in your cache class"
        )
