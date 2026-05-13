class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        output =[0]*len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack or stack[-1][0] >= t:
                stack.append((t,i))
            else:
                while(stack and stack[-1][0] < t):
                    pop = stack.pop()
                    output[pop[1]] = i - pop[1]
                stack.append((t,i))    
        return output            
