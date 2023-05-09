class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph=defaultdict(list)
        ans=[]
        indegree=defaultdict(int)
        for i,j in prerequisites:
            graph[j].append(i)  
            indegree[i]+=1
        queue=deque()
        for x in range (numCourses):
            if indegree[x]==0:
                queue.append(x)

        while queue:
            candidate=queue.popleft()
            ans.append(candidate)
            for node in graph[candidate]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)

        return len(ans)==numCourses
