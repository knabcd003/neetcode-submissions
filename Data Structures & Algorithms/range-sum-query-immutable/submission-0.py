class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = [0] * len(nums)
        self.nums = nums
        for i in range(1, len(self.pre)):
            self.pre[i] = self.pre[i - 1] + nums[i - 1]
    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right] - self.pre[left] + self.nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)