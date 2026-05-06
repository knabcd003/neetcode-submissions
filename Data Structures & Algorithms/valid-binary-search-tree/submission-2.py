# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rightTrav(n, val):
            if not n:
                return True
            if n.val <= val:
                return False
            return rightTrav(n.left, val) and rightTrav(n.right, val)
        def leftTrav(n, val):
            if not n:
                return True
            if n.val >= val:
                return False
            return leftTrav(n.left, val) and leftTrav(n.right, val)
        def dfs(n):
            if not n:
                return True
            #find out how to say everything in the right subtree greater
            #everything in left subtree smaller
            if not leftTrav(n.left, n.val) or not rightTrav(n.right, n.val):
                return False
            return dfs(n.left) and dfs(n.right)
        return dfs(root)
