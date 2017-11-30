class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.id = {}
        self.cap = capacity
        self.pri = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        id = self.cache[key][1]
        del self.id[id]
        self.cache[key][1] = self.pri
        self.id[self.pri] = key
        self.pri += 1
        return self.cache[key][0]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            id = self.cache[key][1]
            del self.id[id]
        elif self.cap > 0:
            self.cap -= 1
        else:
            id = sorted(self.id.keys())[0]
            del self.cache[self.id[id]]
            del self.id[id]
        self.cache[key] = [value, self.pri]
        self.id[self.pri] = key
        self.pri += 1
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)