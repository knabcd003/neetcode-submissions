class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, n in enumerate(nums):
            if target - n in vals:
                return [vals[target - n], i]
            vals[n] = i
        