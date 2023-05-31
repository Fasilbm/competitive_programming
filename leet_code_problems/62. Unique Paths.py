class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        ans =[[0 for i in range(n)] for i in range(m)]
        ans[0][0] = 1
        inbound = lambda row,col: 0 <= row < m and 0 <= col < n

        for i in range(m):
            for j in range(n):
                new_row = i - 1
                new_col = j 
                if inbound(new_row,new_col):
                    ans[i][j] += ans[new_row][new_col]

                new_row = i
                new_col = j - 1
                if inbound(new_row,new_col):
                    ans[i][j] += ans[new_row][new_col]

        return (ans[m-1][n-1])


