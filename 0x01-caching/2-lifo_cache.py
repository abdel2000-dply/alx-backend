#!/usr/bin/env python3
''' LIFO Caching '''
from base_caching import BaseCaching
# You must use self.cache_data - dictionary from the parent class BaseCaching
# You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
# def put(self, key, item):
#   Must assign to the dictionary self.cache_data the item value for the key key.
#   If key or item is None, this method should not do anything.
#   If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
#       you must discard the last item put in cache (LIFO algorithm)
#       you must print DISCARD: with the key discarded and following by a new line
# def get(self, key):
#   Must return the value in self.cache_data linked to key.
#   If key is None or if the key doesn’t exist in self.cache_data, return None.

class LIFOCache(BaseCaching):
    ''' LIFO cache class '''
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Add an item in the cache '''
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discard =  self.keys.pop() # default is -1
                del self.cache_data[discard]
                print('DISCARD:', discard)
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
