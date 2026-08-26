class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix sum: number of elements w that prefix sum
        prefix = {0:1}
        s = 0
        res = 0
        for i in range(0, len(nums)):
            s += nums[i]
            diff = s - k
            res += prefix.get(diff, 0)
            prefix[s] = prefix.get(s, 0) + 1
        return res

