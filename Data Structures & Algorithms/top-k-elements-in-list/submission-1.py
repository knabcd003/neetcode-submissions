class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        arr = [[] for _ in range(len(nums) + 1)]
        for key, v in freq.items():
            arr[v - 1].append(key)
        i = len(arr) - 1
        res = []
        while k > 0:
            for j in arr[i]:
                k -= 1
                res.append(j)
            i -= 1
        return res
        