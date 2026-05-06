class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            piv = (l + r) // 2
            # min between right and piv
            if nums[piv] > nums[r]:
                l = piv + 1
            else:
                r = piv
            print("r", r, "l", l, "p", piv)
        return nums[l]
