class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        firstHalf = self.sortArray(nums[:len(nums)//2])
        secondHalf = self.sortArray(nums[len(nums)//2:])
        f = 0
        s = 0
        i = 0
        while f < len(firstHalf) or s < len(secondHalf):
            if f < len(firstHalf) and s < len(secondHalf):
                if firstHalf[f] > secondHalf[s]:
                    nums[i] = secondHalf[s]
                    s += 1
                else:
                    nums[i] = firstHalf[f]
                    f += 1
            elif f < len(firstHalf):
                nums[i] = firstHalf[f]
                f += 1
            else:
                nums[i] = secondHalf[s]
                s += 1
            i += 1
        return nums
            