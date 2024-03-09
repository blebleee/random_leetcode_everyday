class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2) and nums1[i] != nums2[j]:
            if nums1[i] <= nums2[j]:
                i += 1 
            else:
                j += 1 
        
        if i >= len(nums1) or j >= len(nums2) or nums1[i] != nums2[j]:
            return -1 
        
        return nums1[i]