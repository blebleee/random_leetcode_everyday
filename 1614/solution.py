class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        # f = 0 
        res = 0

        for i in s:
            if i == '(':
                c += 1 
            elif i == ')':
                c -= 1 
            
            res = max(res, c)
        
        return res