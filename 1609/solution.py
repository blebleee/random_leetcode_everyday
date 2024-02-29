def check_strickly_inc(arr):
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            return False

    return True 

def check_strickly_dec(arr):
    for i in range(len(arr)-1):
        if arr[i+1] >= arr[i]:
            return False
             
    return True 
    

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        res = []
        q = [[root, root.val, 0]]
        while q:
            temp = []
            for i in q:
                n, v, l = i
                if v % 2 == l % 2:
                    return False 
                
                if len(res) < l+1:
                    res.append([v])
                else:
                    res[l].append(v)
                
                if n.left:
                    temp.append([n.left, n.left.val, l+1])
                if n.right:
                    temp.append([n.right, n.right.val, l+1])
            
            q = temp 
        
        for idx, i in enumerate(res):
            if idx % 2 == 0:
                if not check_strickly_inc(i):
                    return False 
            else:
                if not check_strickly_dec(i):
                    return False

        return True 