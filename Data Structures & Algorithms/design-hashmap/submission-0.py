class MyHashMap:

    def __init__(self):
        self.hmap = []
        

    def put(self, key: int, value: int) -> None:
        for i, data in enumerate(self.hmap):
            k, v = data
            if k==key:
                self.hmap[i]=[k, value]
                return
        self.hmap.append([key, value])  
        print(self.hmap)      


    def get(self, key: int) -> int:
        for i, data in enumerate(self.hmap):
            k, v = data
            if k==key:
                return self.hmap[i][1]
        return -1        
        

    def remove(self, key: int) -> None:
        for i, data in enumerate(self.hmap):
            k, v = data
            if k==key:
                del(self.hmap[i])
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)