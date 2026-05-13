class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        for t in tokens:
            if t in ["+", "-", "*", "/"] and len(stack) >=2:
                a = stack.pop()
                b = stack.pop()
                print(a,b)

                if t == "+":
                    stack.append(b+a)
                elif t == "-":
                    stack.append(b-a)
                elif t == "*":
                    stack.append(b*a)
                elif t == "/":
                    stack.append(int(float(b)/a))
                print(stack[-1])    
            else:
                stack.append(int(t)) 
        return stack[0]               

#7   
        