class MyHashMap:

    def __init__(self):
        self.storage = []
        

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.storage):
            if key == k:
                self.storage[i] = (key, value)
                return
        self.storage.append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.storage:
            if key == k:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        for i, (k, v) in enumerate(self.storage):
            if key == k:
                del self.storage[i]
                return
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
