class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        inbound= lambda row,col: 0<=row<len(mat) and 0<=col<len(mat[0])
        ans=[[1000 for i in range(len(mat[0]))] for _ in range(len(mat))]
        visited=set()
        queue=deque()
        def bfs(queue,path):
            while queue:
                path+=1
                size=len(queue)
                for _ in range(size):
                    row,col=queue.popleft()
                    for x,y in directions:
                        new_row=row+x
                        new_col=col+y
                        if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                            ans[new_row][new_col]=path
                            queue.append((new_row,new_col))
                            visited.add((new_row,new_col))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j))
                    visited.add((i,j))
                    ans[i][j]=0
                   
        bfs(queue,0)

        return ans
        

