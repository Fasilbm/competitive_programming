class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]==1:
            return -1
        n=len(grid)
        directions=[(1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(-1,0),(0,-1)]
        inbound = lambda row,col: 0<=row<n and 0<=col<n
        target=(n-1,n-1)
        path=0
        visited=set((0,0))
        queue=deque([(0,0)])
        while queue:
            size=len(queue)
            path+=1
            if target in queue:
                return path
            for _ in range(size):
                row,col=queue.popleft()
                for i,j in directions:
                    new_row=row+i
                    new_col=col+j
                    if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                        visited.add((new_row,new_col))
                        if grid[new_row][new_col]==0:
                            queue.append((new_row,new_col))
                            
        return -1
                        

