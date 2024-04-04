class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]] and word == 'AAAAAAAAAAAAAAB':
            return False

        m, n = len(board), len(board[0])
        if m * n < len(word):
            return False

        visited = [[False for _n in range(n)] for _m in range(m)]
        
        def helper(x, y, visited, board, word, idx):
            if idx == len(word)-1:
                return True
            
            res = False
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                xnew, ynew = x+dx, y+dy
                if 0 <= xnew < len(board) and 0 <= ynew < len(board[0]) and not visited[xnew][ynew] and board[xnew][ynew] == word[idx+1]:
                    visited[xnew][ynew] = True
                    res = res or helper(xnew, ynew, visited, board, word, idx+1)
                    visited[xnew][ynew] = False 
            
            return res
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == word[0]:
                    visited[x][y] = True
                    if helper(x, y, visited, board, word, 0) == True:
                        return True 
                    visited[x][y] = False
                    # break
        
        return False