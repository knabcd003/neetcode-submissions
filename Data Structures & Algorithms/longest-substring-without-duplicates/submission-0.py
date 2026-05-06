class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        res = 0
        for r, ch in enumerate(s):
            while ch in chars:
                chars.remove(s[l])
                l += 1
            chars.add(ch)
            res = max(res, r - l + 1)
        return res