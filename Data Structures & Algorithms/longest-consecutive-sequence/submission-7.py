class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elems = set(nums)
        res = 0
        for i in elems:
            if i - 1 not in elems:
                cur = 1
                j = i
                while j + 1 in elems:
                    j += 1
                    cur += 1
                res = max(res, cur)
        return res

        
             

