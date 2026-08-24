class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = Counter(nums)
        i = 0
        while i < freq[0]:
            nums[i] = 0
            i += 1
        while i < freq[0] + freq[1]:
            nums[i] = 1
            i += 1
        while i < len(nums):
            nums[i] = 2
            i += 1
        