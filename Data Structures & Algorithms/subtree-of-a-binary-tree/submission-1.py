# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n, sn):
            if n == None and sn == None:
                return True
            elif n == None or sn == None:
                return False
            return n.val == sn.val and sameTree(n.left, sn.left) and sameTree(n.right, sn.right)
        def dfs(n):
            if n == None:
                return False
            if sameTree(n, subRoot):
                return True
            return dfs(n.left) or dfs(n.right)
        return dfs(root)
        
