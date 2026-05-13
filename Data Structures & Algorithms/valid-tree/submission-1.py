from collections import defaultdict
class Solution:
    def dfs(self, adj, visited, u, parent):
        visited[u] = True
        for v in adj[u]:
            if v == parent:
                continue
            if visited[v] == True:
                return True
            if self.dfs(adj, visited, v, u):
                return True
        return False

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        visited= [False]*n 
        count = 0
        for i in range(n):
            if not visited[i]:
                count +=1
                if count >1:
                    return False
                if self.dfs(adj, visited, i, -1):
                    return False
        return True



        