class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        exits=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        inbound= lambda row,col: 0<=row<len(maze) and 0<=col<len(maze[0])
        for i in range(len(maze[0])):
            if maze[0][i]==".":
                exits.add((0,i))
        for j in range(len(maze)):
            if maze[j][0]==".":
                exits.add((j,0))
        for k in range(len(maze)):
            if maze[k][len(maze[0])-1]==".":
                exits.add((k,len(maze[0])-1))
        for l in range(len(maze[0])):
            if maze[len(maze)-1][l]==".":
                exits.add((len(maze)-1,l))
        queue=deque([(entrance[0],entrance[1])])
        count=0
        visited=set()
        visited.add((queue[0][0],queue[0][1]))
        path=0
        ans=[]
        while queue:
           
            size=len(queue)
            path+=1
            for _ in range(size):
                row,col=queue.popleft()
                for x,y in directions:
                    new_row=x+row
                    new_col=y+col
                    if inbound(new_row,new_col) and maze[new_row][new_col]==".":
                        if (new_row,new_col) in exits and (new_row,new_col) not in visited and (new_row,new_col)!=(entrance[0],entrance[1]):
                            queue.append((new_row,new_col))
                            visited.add((new_row,new_col))
                            return path
                        elif (new_row,new_col) not in visited:
                            queue.append((new_row,new_col))
                            visited.add((new_row,new_col))
            ans.append(path)
        return -1

     
            


        
