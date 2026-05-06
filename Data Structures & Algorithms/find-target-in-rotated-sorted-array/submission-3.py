class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        piv = 0
        while l < r:
            piv = (l + r) // 2
            if nums[piv] > nums[r]:
                l = piv + 1
            else:
                r = piv
        piv = l
        l, r = 0, len(nums) - 1
        if target >= nums[piv] and target <= nums[r]:
            l = piv
        else:
            r = piv - 1
        while l <= r:
            piv = (l + r) // 2
            print(nums[piv])

            if nums[piv] == target:
                return piv
            elif nums[piv] < target:
                l = piv + 1
            else:
                r = piv - 1
        return -1

                