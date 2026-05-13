class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def solve(s, s_, wordDict):
            print("ss")
            if s == s_:
                return True
            if s_ in dp:
                return False    

            for word in wordDict:
                i = len(s_)
                temp = s_
                temp +=word
                # print("i :- ", i)
                # print("temp :-", temp[i: len(temp)])
                # print("s :-", s[i: len(temp)])
                if len(temp) <= len(s) and temp[i: len(temp)] == s[i: len(temp)]:
                    # print("inside")
                    if solve(s, temp, wordDict):
                        return True
                # print("- - -- - -- - - - -- - -  - -")  
            dp[s_] =  False
            print("ddd")
            print(dp)          
            return False 
        return solve(s, "", wordDict)               


        