#!/usr/bin/env python3
''' MRU Caching
'''
from base_caching import BaseCaching
# ou must use self.cache_data - dictionary from the parent class BaseCaching
# You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
# def put(self, key, item):
#   Must assign to the dictionary self.cache_data the item value for the key key.
#   If key or item is None, this method should not do anything.
#   If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
#       you must discard the most recently used item (MRU algorithm)
#       you must print DISCARD: with the key discarded and following by a new line
# def get(self, key):
#   Must return the value in self.cache_data linked to key.
#   If key is None or if the key doesn’t exist in self.cache_data, return None.

class MRUCache(BaseCaching):
    ''' MRU cache class
    '''
    def __init__(self):
        ''' Constructor
        '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is None or item is None:
            return None

        if key in self.cache_data:
            self.order.remove(key)
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.order.pop()
            del self.cache_data[discard]
            print('DISCARD:', discard)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
