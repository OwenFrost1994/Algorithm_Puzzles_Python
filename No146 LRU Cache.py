from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        self.data = OrderedDict()
        self.capacity = capacity
        

    def get(self, key):
        return -1 if key not in self.data else self.data.setdefault(key, self.data.pop(key))
        

    def put(self, key, value):
        if key in self.data:
            self.data.move_to_end(key)
            self.data[key] = value
        else:
            if len(self.data) == self.capacity:
                self.data.popitem(last=False)
            self.data[key] = value

                

lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4

lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(1, 1)
lRUCache.put(2, 3)
lRUCache.put(4, 1)
lRUCache.get(1)
lRUCache.get(2)

lRUCache = LRUCache(2)
lRUCache.get(2)
lRUCache.put(2, 6)
lRUCache.get(1)
lRUCache.put(1, 5)
lRUCache.put(1, 2)
lRUCache.get(1)
lRUCache.get(2)