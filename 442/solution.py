class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in nums:
            if nums[abs(i)-1] < 0:
                res.append(abs(i))
            nums[abs(i)-1] *= -1
                
        
        return res