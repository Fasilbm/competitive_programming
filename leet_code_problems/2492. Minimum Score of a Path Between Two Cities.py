class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:


        size = {i:1 for i in range(1,n+1)}
        rep = {i:i for i in range(1,n+1)}
        weight = {i:float('inf') for i in range(1,n+1)}

        def find(node):
            
            while rep[node] != node:
                node = rep[node]
            return node

        def union(x,y,z):

            parent_x = find(x)
            parent_y = find(y)
            
            if size[parent_x] >= size[parent_y] :
                size[parent_x] += size[parent_y]
                weight[parent_x]= min(weight[parent_x],weight[parent_y],z)
                rep[parent_y] = parent_x
                         
            else:
                size[parent_y] += size[parent_x]
                weight[parent_y]= min(weight[parent_x],weight[parent_y],z)
                rep[parent_x] = parent_y
           
        for i,j,k in roads:

            union(i,j,k)
        rep_1 = find(1)

        return weight[rep_1] 
    

