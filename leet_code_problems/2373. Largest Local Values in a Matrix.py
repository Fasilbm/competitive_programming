class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        else:
            new=[[0]*c for _ in range(r)]
            row=0
            col=0
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    new[row][col]=mat[i][j]
                    col+=1
                    if col==c:
                        col=0
                        row+=1
            return new

            



