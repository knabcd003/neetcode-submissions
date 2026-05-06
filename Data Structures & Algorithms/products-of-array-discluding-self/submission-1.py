class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = set()
        prod = 1
        for i, n in enumerate(nums):
            if n == 0:
                zeroes.add(i)
            else:
                prod *= n
        res = []
        for i, n in enumerate(nums):
            if len(zeroes) > 1:
                res.append(0)
            elif i in zeroes:
                res.append(prod)
            elif len(zeroes) == 0:
                res.append(prod//n)
            else:
                res.append(0)
        return res