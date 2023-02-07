class Solution:
    def spiralOrder(self, matrix):

        n=len(matrix[0])
        m=len(matrix)
        ans=[]
        start_r,start_c=0,0
        row,col=m,n

        for i in range(n*m):

            if start_r==row:
                break
            for j in range(start_c,col):
                ans.append(matrix[start_r][j])
            start_r+=1
            if start_r==row:
                break
            for k in range(start_r,row):
                ans.append(matrix[k][col-1])
            col-=1
            if start_c==col:
                break
            for l in range(col-1,start_c,-1):
                ans.append(matrix[row-1][l])
            row-=1
            if start_c==col:
                break
            for m in range(row,start_r-1,-1):
                ans.append(matrix[m][start_c])
            start_c+=1
            if start_c==col:
                break
            print(ans)
        return ans
