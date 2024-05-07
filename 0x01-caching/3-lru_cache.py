#!/usr/bin/env python3
''' LRU Caching
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    ''' LRU cache class
    '''
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is None or item is None:
            return None
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.order.pop(0)
            del self.cache_data[discard]
            print('DISCARD:', discard)

        if key in self.cache_data:
            self.order.remove(key)
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
