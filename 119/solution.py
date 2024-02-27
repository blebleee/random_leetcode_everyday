class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1], [1,1]]

        for i in range(2, rowIndex + 1):
            pascal.append([1])
            for j in range(1, len(pascal[i-1])):
                pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
            
            pascal[i].append(1)

        return pascal[rowIndex]
        