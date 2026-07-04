class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                p = st.pop()
                res[p] = i - p
            st.append(i)
        for i in st:
            res[i] = 0
        return res

