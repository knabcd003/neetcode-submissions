class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for n, c in enumerate(strs[0]):
            for i in range(1, len(strs)):
                if n >= len(strs[i]) or strs[i][n] != c:
                    return ''.join(res)
            res.append(c)
        return ''.join(res)