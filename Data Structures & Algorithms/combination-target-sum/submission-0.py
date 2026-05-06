import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def backtrack(s, i):
            if s == target:
                res.append(copy.deepcopy(cur))
                return
            if s > target or i >= len(nums):
                return
            s += nums[i]
            cur.append(nums[i])
            backtrack(s, i)
            s -= nums[i]
            cur.pop()
            backtrack(s, i + 1)
        backtrack(0, 0)
        return res