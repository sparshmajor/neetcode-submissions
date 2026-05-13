from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counted = sorted(list(Counter(nums).items()), key =lambda x:x[1])
        res=[]
        i =0
        while(i < len(counted)-1):
            if counted[i][1] == counted[i+1][1]:
                temp =[]
                while(i < len(counted)-1 and counted[i][1] == counted[i+1][1]):
                    temp.append(counted[i])
                    i+=1
                temp.append(counted[i])
                print("temp",temp)
                temp.sort()
                res.extend(temp[::-1])
            else:
                res.append(counted[i]) 
            i+=1 
        if i < len(counted):     
            res.append(counted[i])     
        print(res)      
        final =[]    
        for i, j in res:
            for _ in range(j):
                final.append(i)
        return final