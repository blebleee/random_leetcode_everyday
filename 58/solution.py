class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = []
        f = 0
        for idx, i in enumerate(s):
            if i != ' ':
                if f == 0:
                    st.append(i)
                else:
                    st = [i]
                    f = 0
            else:
                f = 1 
        
        print(st)
        return len(st)