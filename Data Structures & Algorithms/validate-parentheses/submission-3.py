class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        opening = {'(', '[', '{'}
        closing = {')': '(',
                    '}': '{',
                    ']': '['}
        for i, ch in enumerate(s):
            if ch in opening:
                st.append(ch)
            else:
                if st and st[-1] == closing[ch]:
                    st.pop()
                else:
                    return False
        return not st