class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token in operators:
                second = st.pop()
                first = st.pop()
                if token == '+':
                    st.append(first + second)
                if token == '-':
                    st.append(first - second)
                if token == '*':
                    st.append(first * second)
                if token == '/':
                    st.append(int(first / second))
            else:
                st.append(int(token))
        return st[-1]