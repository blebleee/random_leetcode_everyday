class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        c0, c1 = 0, 0 
        d[0] = [-1]

        for idx, i in enumerate(nums):
            if i == 0:
                c0 += 1 
            else:
                c1 += 1 
            
            t = c0 - c1 
            if t not in d:
                d[t] = [idx] 
            else:
                d[t].append(idx)
        
        maxx = 0
        for k, v in d.items():
            if len(v) >= 2:
                maxx = max(maxx, v[-1] - v[0])
        
        return maxx