class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1 
        
        res = -1 
        for k, v in d.items():
            if k > 0:
                if -k in d:
                    res = max(res, k) 
            
        
        return res