# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = deque()
        q.append(root)
        level = 1
        res = []
        while q:
            cur = []
            children = 0
            for i in range(level):
                tmp = q.popleft()
                cur.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                    children+=1
                if tmp.right:
                    q.append(tmp.right)
                    children += 1
            level = children
            res.append(cur)
        return res

