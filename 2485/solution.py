class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        # return int(sqrt((n*n+n)//2))
        s = n * (n+1) // 2
        
        curr = 1
        for i in range(2, n):
            curr += i 
            if curr == s - curr + i:
                return i 
        
        return -1