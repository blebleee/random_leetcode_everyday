# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        res = []
        def helper(r, s):
            s += chr(r.val+97)
            
            if not r.right and not r.left:
                res.append(s[::-1]) 
                pass
            elif not r.right:
                helper(r.left, s)
            elif not r.left:
                helper(r.right, s)
            else:
                helper(r.left, s)
                helper(r.right, s)
        
        helper(root, '')
        print(res)
        return min(res)