class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        a, b = -1, -1 
        f = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                a = i - 1 
                b = i + 1 
                f = 1 
                break 
            
            elif i != len(nums) -1 and nums[i] * nums[i+1] < 0:
                a = i 
                b = i + 1 
                break 
        
        if a == b == -1:
            if nums[0] > 0:
                return [i*i for i in nums] 
            else:
                return [i*i for i in reversed(nums)]
        
        res = []
        if f == 1:
            res.append(0)
        
        while a >= 0 or b < len(nums):
            if a >= 0 and b < len(nums):
                if nums[a] ** 2 <= nums[b] ** 2:
                    res.append(nums[a] ** 2)
                    a -= 1 
                else:
                    res.append(nums[b] ** 2)
                    b += 1 

            elif a >= 0:
                res.append(nums[a] ** 2)
                a -= 1 
            elif b < len(nums):
                res.append(nums[b] ** 2)
                b += 1 
        
        return res
             
            