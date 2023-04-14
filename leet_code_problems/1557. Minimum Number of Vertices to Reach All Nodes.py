class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        # def dfs(node,adj_list,visited):
        #     visited.add(node)
        #     for i in adj_list[node]:
        #         if i not in visited:
        #             dfs(i,adj_list,visited)
        adj_list={}
        for i in range(n):
            adj_list[i]=[]
        for i,j in edges:
            adj_list[j].append(i)
        self.ans=[]
        # visited=set()
        for node in adj_list.keys():
            if adj_list[node]==[]:
                self.ans.append(node)
        return self.ans
