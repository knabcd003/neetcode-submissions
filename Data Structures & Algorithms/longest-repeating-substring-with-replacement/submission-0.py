class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxch = s[0]
        maxv = 1
        l = 0
        res = 0
        for r, ch in enumerate(s):
            freq[ch] = freq.get(ch, 0) + 1
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
