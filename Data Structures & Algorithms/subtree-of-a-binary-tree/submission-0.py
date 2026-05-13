# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes =[]
        def find_node_pos(root, node):
            nonlocal nodes
            if root== None:
                return
            if root.val == node.val:
                nodes.append(root)    

            find_node_pos(root.left, node)
            find_node_pos(root.right, node)
        def check_same_tree(root, subroot):
            if root== None and subroot== None:
                return True
            if root and subroot and root.val == subroot.val:
                left = check_same_tree(root.left, subroot.left)   
                right = check_same_tree(root.right, subroot.right)
                return left and right
        find_node_pos(root, subRoot)        
        for n in nodes:
            if check_same_tree(n, subRoot):
                return True
        return False        




        