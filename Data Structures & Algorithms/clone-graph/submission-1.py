"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map  = {}
        # print(node.val)
        # print([v.val for v in node.neighbors])
        def dfs(node):
            # print(node.val)
            if node in map:
                return map[node]

            root = Node(node.val)

            map[node] = root
            for v in node.neighbors:
                res = dfs(v)
                root.neighbors.append(res)
            return root       
        return dfs(node) if node else None