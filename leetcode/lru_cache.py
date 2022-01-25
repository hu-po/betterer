from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity : int = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()
        self.last_value: int = None

    def get(self, key: int) -> int:
        if self.cache.get(key, None) is not None:
            self.last_value = self.cache[key]
            del self.cache[key]
            self.cache[key] = self.last_value
            return self.last_value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, None) is not None:
            # re-position the new element to the front of the ordered dict
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # delete least recently used item
            del self.cache[next(key for key in self.cache.keys())]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
