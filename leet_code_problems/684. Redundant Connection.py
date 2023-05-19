class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        rep = {i:i for i in range(1,len(edges)+1)}
        ans= []
        def find(node):
            while rep[node] != node:
                node = rep[node]
            return node

        def union(x,y):
            parent_x = find(x)
            parent_y = find(y)

            if parent_x == parent_y:
                ans.append(x)
                ans.append(y)
                return
            rep[parent_y] = rep[parent_x]

        for i,j in edges:
            union(i,j)
            if ans:
                break

        return (ans)
