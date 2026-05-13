from collections import defaultdict
class Solution:
    def dfs(self, visited, u, adj):
        visited[u]=True
        for v in adj[u]:
            if not visited[v]:
                self.dfs(visited, v, adj)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visited =[False]*n
        count = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(visited, i, adj) 
                count+=1
        return count           



        