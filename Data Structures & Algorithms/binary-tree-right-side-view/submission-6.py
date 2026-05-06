# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        def helper(n):
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        while q:
            level = len(q)
            for i in range(level - 1):
                cur = q.popleft()
                helper(cur)
            final = q.popleft()
            helper(final)
            res.append(final.val)
        return res
