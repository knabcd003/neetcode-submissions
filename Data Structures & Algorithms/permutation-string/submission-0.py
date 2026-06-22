class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        freq2 = {}
        l = 0
        for r in range(len(s2)):
            freq2[s2[r]] = freq2.get(s2[r], 0) + 1
            while r - l + 1 > len(s1):
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    freq2.pop(s2[l])
                l += 1
            if freq1 == freq2:
                return True
        return False
             