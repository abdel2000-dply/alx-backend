#!/usr/bin/env python3
''' LFU Caching
'''
from base_caching import BaseCaching
from collections import defaultdict


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
