class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            pivot = (r + l) // 2
            if nums[pivot] > nums[r]:
                l = pivot + 1
            else:
                r = pivot
        return nums[l]
