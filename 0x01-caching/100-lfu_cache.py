#!/usr/bin/env python3
''' LFU Caching
'''
from base_caching import BaseCaching
from collections import defaultdict
# Create a class LFUCache that inherits from BaseCaching and is a caching system:

# You must use self.cache_data - dictionary from the parent class BaseCaching
# You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
# def put(self, key, item):
#   Must assign to the dictionary self.cache_data the item value for the key key.
#   If key or item is None, this method should not do anything.
#   If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
#       you must discard the least frequency used item (LFU algorithm)
#       if you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used
#       you must print DISCARD: with the key discarded and following by a new line
# def get(self, key):
#   Must return the value in self.cache_data linked to key.
#   If key is None or if the key doesn’t exist in self.cache_data, return None.

class LFUCache(BaseCaching):
    ''' LFU cache class
    '''
    def __init__(self):
        ''' Constructor
        '''
        super().__init__()
        self.lft = defaultdict(int)

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is None or item is None:
            return None

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_frq = min(self.lft.values())
            discard = [k for k, v in self.lft.items() if v == min_frq]
            if len(discard) > 1:
                # Use LRU to break ties
                lru_item = min(discard, key=lambda x: self.cache_data[x])
                discard.remove(lru_item)
            for k in discard:
                del self.cache_data[k]
                del self.lft[k]
                print('DISCARD:', k)

        self.cache_data[key] = item
        self.lft[key] += 1

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        self.lft[key] += 1
        return self.cache_data[key]
            
