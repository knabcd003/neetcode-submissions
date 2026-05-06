# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #last value we find p <= val <= q
        less = min(p.val, q.val)
        more = max(p.val, q.val)
        def dfs(root):
            if root == None:
                return None
            if root.val >= less and root.val <= more:
                return root
            elif root.val >= more:
                return dfs(root.left)
            return dfs(root.right)
        return dfs(root)