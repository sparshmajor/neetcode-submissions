from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for v, u in prerequisites:
            adj[u].append(v)

        indegree =[0]*numCourses
        for i in range(numCourses):
            for v in adj[i]:
                indegree[v]+=1
        # print(indegree)
        q =[]
        for i, j in enumerate(indegree):
            if j == 0:
                q.append(i)
        res = []        
        while q:
            u = q.pop(0)
            res.append(u)
            for v in adj[u]:
                indegree[v]-=1
                if  indegree[v] == 0:
                    q.append(v)
        # print(res)            
        if len(res) != len(indegree):
            return False
        return True                                       