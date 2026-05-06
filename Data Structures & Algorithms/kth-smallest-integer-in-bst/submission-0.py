# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(n, index):
            if not n:
                return -1
            tmp = dfs(n.left, index)
            if tmp != -1:
                return tmp
            index[0] += 1
            if index[0] == k:
                return n.val
            return dfs(n.right, index)
        return dfs(root, [0])