class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        location=[]
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    location.append([i,j])
     
        for i,j in location:
            for k in range(row):
                for l in range(col):
                    if k==i or j==l:
                        matrix[k][l]=0
        
          
