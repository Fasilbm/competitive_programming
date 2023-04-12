class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
        adj_list={}
        for i in range(len(graph)):
            adj_list[i]=[]
            for j in graph[i]:
                adj_list[i].append(j)
        self.ans=[]
        target=len(graph)-1
        def dfs(comb,node):
            if node==target:
                comb.append(node)
                self.ans.append(comb.copy())
                return
            comb.append(node)
            for i in adj_list[node]:
                dfs(comb,i)
                comb.pop()
        dfs([],0)
        return self.ans
           
            
