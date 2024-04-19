class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root) 
        
        def dfs(node, level):
            if level == depth - 1:  
                node.left = TreeNode(val, left=node.left) if node.left else TreeNode(val)
                node.right = TreeNode(val, right=node.right) if node.right else TreeNode(val)
                return node
            else:  
                if node.left: node.left = dfs(node.left, level+1)
                if node.right: node.right = dfs(node.right, level+1)
                return node
            
        
        root = dfs(root, 1)  
        return root