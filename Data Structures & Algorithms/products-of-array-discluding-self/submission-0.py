class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroes = 0
        for i, n in enumerate(nums):
            if n != 0:
                product *= n
            else:
                zeroes += 1
        res = []
        for i, n in enumerate(nums):
            if zeroes > 1:
                res.append(0)
            elif n == 0:
                res.append(product)
            elif zeroes == 1:
                res.append(0)
            else:
                res.append(product//n)
        return res