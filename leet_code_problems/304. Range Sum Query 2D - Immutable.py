class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col=len(matrix),len(matrix[0])
        self.prefix_matrix=[[0]*(col+1)for i in range(row+1)]
        for r in range(row):
            prefix=0
            for c in range(col):
                prefix+=matrix[r][c]
                above=self.prefix_matrix[r][c+1]
                self.prefix_matrix[r+1][c+1]=prefix+above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        above=self.prefix_matrix[row1-1][col2]
        left=self.prefix_matrix[row2][col1-1]
        bottom_right=self.prefix_matrix[row2][col2]
        top_left=self.prefix_matrix[row1-1][col1-1]
        return bottom_right-above-left+top_left
    # Time complexity O(n^2)
    # Space complexity O(n^2)
    
        
         
         


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
