class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        rep = {i:i for i in range(len(s))}
        size = {i:1 for i in range(len(s))}
        def find(node):
            while rep[node] != node:
                node = rep[node]
            return node

        def union(x,y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if size[parent_x] >= size[parent_y] :
                    size[parent_x] += size[parent_y]
                    rep[parent_y] = parent_x         
                else:
                    size[parent_y] += size[parent_x]
                    rep[parent_x] = parent_y

        for i,j in pairs:
            union(i, j)

        parents = defaultdict(list)
        for key in rep.keys():
            fetch = find(key)
            parents[fetch].append(s[key])

        ans = ""
        for key in parents.keys():
            parents[key].sort(reverse = True)
        
        for i in range(len(s)):
            fetch = find(i)
            ans += parents[fetch].pop()

        return (ans)
            



        
