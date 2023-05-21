class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        rep = {s1[i]:s1[i] for i in range(len(s1))}
        rep2 = {s2[i]:s2[i] for i in range(len(s2))}
        rep.update(rep2)
        group = defaultdict(set)

        def find(node):
           
            while rep[node] != node :
                node = rep[node]
            return node
        
        def union(x,y):

            parent_x = find(x)
            parent_y = find(y)
            if parent_x > parent_y :
                rep[parent_x] = rep[parent_y]
            else:
                rep[parent_y] = rep[parent_x]

        for i in range(len(s1)):
            union(s1[i],s2[i])

        ans = ""
        
        for i in baseStr:
            if i in rep: 
                par = find(i)
            else:
                par = i

            ans += par

        return (ans)
                

            
