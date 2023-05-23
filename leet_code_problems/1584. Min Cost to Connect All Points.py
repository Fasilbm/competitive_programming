class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edge = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                edge.append((points[i], points[j], abs(points[i][0]-points[j][0])+\
                abs(points[i][1] - points[j][1])))

        edge.sort(key = lambda x:x[2])
        rep = {tuple(points[i]):tuple(points[i] )for i in range(len(points))}
        
        def find(node):

            while rep[node] != node :
                node = rep[node]
            return node

        def union(x,y):
            
            parent_x = find(x)
            parent_y = find(y)
            rep[parent_y] = rep[parent_x]
            
        cost = 0
        
        for i in range(len(edge)):
            if find(tuple(edge[i][0])) != find(tuple(edge[i][1])) :

                cost += edge[i][2]
                union(tuple(edge[i][0]), tuple(edge[i][1]))

        return (cost)

        


        
        


        


    
