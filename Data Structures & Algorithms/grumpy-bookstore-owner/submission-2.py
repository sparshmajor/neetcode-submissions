class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        x = [-float('inf'), [-1,-1]]
        for i in range(len(customers)-minutes+1):
            s = sum([ a*b for a,b in zip(customers[i:i+minutes], grumpy[i:i+minutes])])
            if x[0] < s:
                x[0] = s
                x[1] = [i, i+minutes-1]
        z = sum(customers[x[1][0]: x[1][1]+1])        
        y = 0
        for i in range(len(customers)):
            if grumpy[i] == 0 and (i not in range(x[1][0], x[1][1]+1)):
                y+=customers[i]
        return z + y                  

# customers  =  [ 4, 10, 10 ]
# grumpy     =  [ 1, 1, 0 ]   
# minutes    =  [ 2 ]        