from collections import defaultdict
import heapq
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set("".join(wordList))
        set_wordList = set(wordList)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                for c in s:
                    temp = word
                    if temp[i]== c:
                        continue   
                    temp = temp[:i] + c + temp[i+1:]
                    if temp in set_wordList:
                        adj[word].append(temp)
        print("graph",adj)

        cost = {}
        for key, value in adj.items():
            cost[key]= float('inf')  
        print("initial",cost)    

        source = beginWord 
        flag =0
        if beginWord not in set_wordList:
            flag =1
            for i in range(len(beginWord)):            
                for c in s:
                    temp = beginWord
                    if temp[i]== c:
                        continue
                    temp = temp[:i] + c + temp[i+1:]    
                    if temp in adj.keys():
                        source = temp
                        break   
        q =[] 
        print("source", source)
        cost[source] = 0
        heapq.heappush(q, (0,source))
        while(q):
            dis, u = heapq.heappop(q)
            for v in adj[u]:
                if cost[v] > dis+1:
                    cost[v] = dis+1
                    heapq.heappush(q,(dis+1, v))
        if endWord not in cost or cost[endWord]==float('inf'):
            return 0   
        return cost[endWord]+1+flag

        