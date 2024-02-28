class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = [[root.val]]
        q = [[root, root.val, 0]]

        while q:
            temp = []
            for node, val, level in q:
                if len(res) == level:
                    res.append([val])
                else:
                    res[level].append(val)

                if node.left:
                    temp.append([node.left, node.left.val, level+1])
                if node.right:
                    temp.append([node.right, node.right.val, level+1])
            
            q = temp
        
        return res[-1][0]