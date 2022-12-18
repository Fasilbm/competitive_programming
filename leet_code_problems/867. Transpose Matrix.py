class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        row,col=len(matrix),len(matrix[0])
        res=[[0] * row for i in range(col)]
        for j in range(row):
            for k in range(col):
                res[k][j]=matrix[j][k]
        return res
