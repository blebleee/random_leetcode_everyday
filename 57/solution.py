class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        if intervals == []:
            return [new]
        if new[1] < intervals[0][0]:
            return [new] + intervals

        st = []
        f = 0
        for s, e in intervals:
            if e < new[0] or s > new[1]:
                st.append([s, e])
            else:
                if f == 0:
                    s1 = min(s, new[0])
                    e1 = max(e, new[1])
                    st.append([s1, e1])
                    f = 1 
                else:
                    s1, e1 = st.pop()
                    s1 = min(s1, s)
                    e1 = max(e1, e)
                    st.append([s1, e1])
        
        if f == 0:
            idx = -1
            # st.append([new[0], new[1]])
            for i in range(len(st)-1):
                if st[i][1] < new[0] < st[i+1][0]:
                    idx = i 
                    break 
            
            if idx != -1:
                st = st[:idx+1] + [new] + st[idx+1:]
            else:
                st = st + [new]

        return st 
