class Solution:
    def trap(self, height: List[int]) -> int:
       lm = 0
       l = 0
       rm = 0
       r = len(height)-1
       profit =0
       while (l<r):
            lm = max(height[l], lm)
            rm = max(height[r], rm)
        
        
            if height[l] <= height[r]:
                if lm - height[l] > 0:
                    profit += (lm - height[l])
                print("left",l,r, profit)    

                l+=1
            else:
                if rm - height[r] > 0:
                    profit += (rm - height[r])
                print("right",l,r, profit)    
                r-=1 
                  
       return profit     









        