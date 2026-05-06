# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n, smallest, largest):
            if not n:
                return True
            if n.val <= smallest or n.val >= largest:
                return False
            return dfs(n.left, smallest, n.val) and dfs(n.right, n.val, largest)
        return dfs(root, float('-inf'), float('inf'))
