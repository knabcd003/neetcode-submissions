class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            alpha = [0] * 26
            for l in word:
                alpha[ord(l) - ord('a')] += 1
            s = str(alpha)
            words[s] = words.get(s, []) + [word]
        return list(words.values())