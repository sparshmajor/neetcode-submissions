from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(adj, u, visited, dest, parent, res):
            if u == dest:
                return True
            visited.add(u)
            for wt , v in adj[u]:
                if v == parent:
                    continue
                res.append((v, wt))
                if v not in visited:
                    if dfs(adj, v, visited, dest, u, res):
                        return True
                    res.pop()
            return False            
        
        adj = defaultdict(list)
        for i, node in enumerate(equations):
            u,v = node
            wt = values[i]
            adj[u].append((wt, v))
            adj[v].append((1/wt,u))
        result =[]
        for src, dest in queries:
            print(f"\nQuery: {src} -> {dest}")
            if src not in adj or dest not in adj:
                print("No such variable.")
                result.append(-1)
                continue

            visited = set()
            path = []
            
            if dfs(adj, src,  visited, dest, -1, path):
                print("Path found:", [(src, 1.0)] + path)
                mul= 1
                for node, value in path:
                    mul *= value
                result.append(mul)
            else:
                result.append(-1)
        return result    
