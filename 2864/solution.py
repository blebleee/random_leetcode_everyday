class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c1, c0 = 0, 0
        for i in s:
            if i == '0':
                c0 += 1 
            else:
                c1 += 1 
        
        if c1 == 1:
            return '0' * c0 + '1'
        else:
            return '1' * (c1-1) + '0' * c0 + '1'