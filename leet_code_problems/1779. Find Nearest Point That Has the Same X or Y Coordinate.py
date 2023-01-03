class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        distances={}
        for i in range(len(points)):
            j=0
            if points[i][j]==x:
                man_dist=abs(x-points[i][j])+abs(y-points[i][j+1])
                if man_dist in distances:
                    continue
                else:
                    distances[man_dist]=i
            elif points[i][j+1]==y:
                man_dist=abs(x-points[i][j])+abs(y-points[i][j+1])
                if man_dist in distances:
                    continue
                else:
                    distances[man_dist]=i
        if len(distances)==0:
            return -1
        else:
            return distances[min(distances)]
        
        
