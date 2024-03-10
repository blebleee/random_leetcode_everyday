class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = {}, {}
        for i in nums1:
            d1[i] = 1 
        
        res = []

        for i in nums2:
            if i in d1 and i not in d2:
                res.append(i)
            
            d2[i] = 1 
        
        return res