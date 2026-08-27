class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minword = word1 if len(word1) < len(word2) else word2
        maxword = word1 if len(word1) >= len(word2) else word2
        res = []
        for i in range(len(minword)):
            res.append(word1[i])
            res.append(word2[i])
        for i in range(len(minword), len(maxword)):
            res.append(maxword[i])
        return "".join(res)