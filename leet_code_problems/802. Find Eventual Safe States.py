class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        outdegree=defaultdict(int)
        dependecies=defaultdict(list)
        for i,j in enumerate(graph):
            outdegree[i]=len(j)
            for ele in j:
                dependecies[ele].append(i)
        queue=deque()
        for key in outdegree.keys():
            if outdegree[key]==0:
                queue.append(key)

        while queue:
            candidate=queue.popleft()
            for node in dependecies[candidate]:
                outdegree[node]-=1
                if outdegree[node]==0:
                    queue.append(node)

        ans=[]
        for key in outdegree.keys():
            if outdegree[key]==0:
                ans.append(key)

        return ans
        
