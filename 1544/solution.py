class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in s:
            if not st:
                st.append(i)
            else:
                if i.lower() == st[-1].lower() and i != st[-1]:
                    st.pop()
                else:
                    st.append(i)
        
        return "".join(st)