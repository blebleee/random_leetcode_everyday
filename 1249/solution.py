class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        op, cl = [], []

        for idx, i in enumerate(s):
            if i == '(':
                op.append(idx)
            elif i == ')':
                if op and idx > op[-1]:
                    op.pop()
                else:
                    cl.append(idx)
        
        res = ''

        j, k = 0, 0

        for idx, i in enumerate(s):
            if i == '(':
                if op and j < len(op) and idx == op[j]:
                    j += 1
                    continue 
                
            elif i == ')':
                if cl and k < len(cl) and idx == cl[k]:
                    k += 1 
                    continue 
            
            res += i 
        
        return res