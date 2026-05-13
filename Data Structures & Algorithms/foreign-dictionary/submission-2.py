class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # we will use topo sort to solve this problem 
        adj = {c:set() for w in words for c in w}
        indegree = {c: 0 for c in adj}
        i=0
        for j in range(1, len(words)):
            w1 = words[i]
            w2 = words[j]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for c1, c2 in zip(w1,w2):
                if c1==c2:
                    continue
                else:
                    adj[c1].add(c2)  
                break                  
            i = j    

        for u, v in adj.items():
            for node in v:
                indegree[node] = indegree.get(node,0) + 1

        # print(indegree) 
        q= []
        for u, v in indegree.items():
            if v ==0:
                q.append(u)
        res=[]
        while(q):
            u = q.pop()
            res.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res )           
















        

        