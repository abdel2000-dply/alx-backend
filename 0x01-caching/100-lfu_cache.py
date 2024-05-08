#!/usr/bin/env python3
''' LFU Caching
'''
from base_caching import BaseCaching
from collections import Counter, OrderedDict


class LFUCache(BaseCaching):
    ''' LFU cache class
    '''
    def __init__(self):
        ''' Constructor
        '''
        super().__init__()
        self.lfu = Counter()
        self.order = OrderedDict()

    def put(self, key, item):
        ''' Add an item in the cache
        '''
        if key is None or item is None:
            return None

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = min(
                self.order, key=lambda k: (self.lfu[k], self.order[k]))
            del self.cache_data[discard]
            del self.lfu[discard]
            del self.order[discard]
            print('DISCARD:', discard)

        self.cache_data[key] = item
        self.lfu[key] += 1
        self.order[key] = len(self.order)

    def get(self, key):
        ''' Get an item by key
        '''
        if key is None or key not in self.cache_data:
            return None
        self.lfu[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]
