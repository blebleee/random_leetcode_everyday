class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # not an optimal solution
        d = {}
        for i in nums:
            if i > 0:
                d[i] = 1 
        
        t = 1 
        while t in d:
            t += 1 
        
        return t