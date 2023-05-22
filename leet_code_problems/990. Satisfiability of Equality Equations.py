class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        rep = {chr(i):chr(i) for i in range(97,123)}

        def find(node):

            while rep[node] != node :
                node = rep[node]
            return node

        def union(x,y):

            parent_x = find(x)
            parent_y = find(y)
            rep[parent_y]  = rep[parent_x]

        for i in range(len(equations)):

            if equations[i][1] == "=" :

                union(equations[i][0],equations[i][3])

        for i in range(len(equations)):

              if equations[i][1] == "!" and (find(equations[i][0])==find(equations[i][3])):

                  return False

        return True

            
        





        
