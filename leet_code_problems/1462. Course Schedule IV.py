class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph=defaultdict(list)
        indegree=defaultdict(int)
        ancestors=defaultdict(set)

        for i,j in prerequisites:
            graph[i].append(j)
            indegree[j]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            candidate=queue.popleft()
            for node in graph[candidate]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
                ancestors[node].add(candidate)
                ancestors[node].update(ancestors[candidate])

        ans=[]
        print(ancestors)
        for i,j in queries:
            if i in ancestors[j]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


