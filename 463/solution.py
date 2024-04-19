class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    c = 0
                    if i == 0:
                        c += 1
                    if i == len(grid) - 1:
                        c += 1
                    if j == 0:
                        c += 1
                    if j == len(grid[0]) - 1:
                        c += 1

                    for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        new_i = i + di 
                        new_j = j + dj 
                        if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                            if grid[new_i][new_j] == 0:
                                c += 1 
                        
                    # print(c)
                    res += c 

        
        return res