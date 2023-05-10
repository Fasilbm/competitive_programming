class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ans=defaultdict(set)
        ancestor=defaultdict(list)
        indegree=defaultdict(int)
        res=[[] for i in range(n)]
        for i,j in edges:
            ancestor[i].append(j)
            indegree[j]+=1

        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            candidate=queue.popleft()
            for node in ancestor[candidate]:

                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
                ans[node].add(candidate)
                ans[node].update(ans[candidate])
        for i in ans:
            res[i]=sorted(list(ans[i]))
             
        return (res)     


        


       
