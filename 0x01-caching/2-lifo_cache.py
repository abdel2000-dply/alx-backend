#!/usr/bin/env python3
''' LIFO Caching
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    ''' LIFO cache class
    '''
    def __init__(self):
        ''' Constructor
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discard = self.keys.pop()  # default is -1
                del self.cache_data[discard]
                print('DISCARD:', discard)
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
