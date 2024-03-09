class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        
        res = 0 
        maxx = 0

        for k, v in d.items():
            if v > maxx:
                maxx = v 
                res = v 
            elif v == maxx:
                res += v
        
        return res