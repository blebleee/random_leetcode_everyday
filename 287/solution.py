class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in nums:
            nums[abs(i)] *= -1

            if nums[abs(i)] > 0:
                return abs(i)