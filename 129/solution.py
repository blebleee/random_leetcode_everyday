# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        nums = []
        
        def dfs(r, s):
            # 1 
            # 1 2
            s = s*10 + r.val 
            
            if r.left:
                dfs(r.left, s)
            if r.right:
                dfs(r.right, s)
            
            if not r.left and not r.right:
                nums.append(s)
                return 
        
        dfs(root, 0)
        return sum(nums)