from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        def dfs(adj, u, visited, parent):
            visited[u] = True
            for v in adj[u]:
                if v == parent:
                    continue
                if visited[v]:
                    return True    
                if dfs(adj, v, visited, u):
                    return True
            return False    
        for u, v in edges:
            print(u,v)
            adj[u].append(v)
            adj[v].append(u)
            visited =[False]* (len(edges)+1)
            print(visited)
            if dfs(adj, u, visited, -1):
                return [u,v]




        