# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue =[root]
        result = []
        while True:
            _queue = []
            _result = []
            while queue:
                node = queue.pop(0)
                _result.append(node.val)
                if node.left:
                    _queue.append(node.left)
                if node.right:    
                    _queue.append(node.right)
            result.append(_result)
            queue = _queue
            if len(queue) == 0:
                break
        return result        

