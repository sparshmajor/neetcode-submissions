class MyHashSet:

    def __init__(self):
        self.hset = []
        

    def add(self, key: int) -> None:
        for i in self.hset:
            if i ==key:
                return
        self.hset.append(key)        


    def remove(self, key: int) -> None:
        for i,j in enumerate(self.hset):
            if j == key:
                del(self.hset[i])
        

    def contains(self, key: int) -> bool:
        for i in self.hset:
            if i ==key:
                return True
        return False        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)