class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node,visited,graph):
            visited.add(node)
            for node in graph[node]:
                if node not in visited:
                    dfs(node,visited,graph)

        count=0
        def adj_list(isConnected):
            from collections import defaultdict
            graph=defaultdict()
            for i in range(len(isConnected)):
                graph[i+1]=[]
            for i in range(len(isConnected)):
                for j in range(len(isConnected)):
                    if isConnected[i][j]==1 and i!=j:
                        graph[i+1].append(j+1)
            visited=set()
            nonlocal count
            for key in graph.keys():
                if key not in visited:
                    dfs(key,visited,graph)
                    count+=1
        adj_list(isConnected)
        return count

        
                
