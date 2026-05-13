class StockSpanner:

    def __init__(self):
        self.stack =[]
        

    def next(self, price: int) -> int:
        if not self.stack or self.stack[-1][0] > price:
            self.stack.append((price,1))
            return 1
        else:
            res=1
            while(self.stack and self.stack[-1][0] <= price):
                el, v = self.stack.pop()
                res+=v
            self.stack.append((price, res))    
            return res 



                


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)