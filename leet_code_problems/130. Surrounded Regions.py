class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions=[(0,-1),(0,1),(1,0),(-1,0)]
        visited=set()
        uncaptured=set()
        m=len(board)
        n=len(board[0])
        inbound = lambda row,col: 0<=row<m and 0<=col<n
        def dfs(board,row,col,visited):
            visited.add((row,col))
            for i,j in directions:
                new_row=i+row
                new_col=j+col

                if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                    if board[new_row][new_col]=="O":
                        uncaptured.add((new_row,new_col))
                        dfs(board,new_row,new_col,visited)
        for l in range(n):
            if board[m-1][l]=="O" and (m-1,l) not in visited:
                uncaptured.add((m-1,l))
                dfs(board,m-1,l,visited)
        for i in range(m):
            if board[i][0]=="O" and (i,0) not in visited:
                uncaptured.add((i,0))
                dfs(board,i,0,visited)
        for j in range(n):
            if board[0][j]=="O" and (0,j) not in visited:
                uncaptured.add((0,j))
                dfs(board,0,j,visited)
        for k in range(len(board)):
            if board[k][n-1]=="O" and (k,n-1) not in visited:
                uncaptured.add((k,n-1))
                dfs(board,k,n-1,visited)
        for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j]=="O" and (i,j) not in uncaptured:
                            board[i][j]="X"
                                        



            
            
