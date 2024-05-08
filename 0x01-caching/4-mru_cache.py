#!/usr/bin/env python3
''' MRU Caching
'''
from base_caching import BaseCaching


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
