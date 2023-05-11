class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        ans=defaultdict(set)
        ancestor=defaultdict(list)
        indegree=defaultdict(int)
        res=[[] for i in range(len(quiet))]
        final=[]

        for i,j in richer:
            ancestor[i].append(j)
            indegree[j]+=1

        queue=deque()
        for i in range(len(quiet)):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            candidate=queue.popleft()
            for node in ancestor[candidate]:

                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
                ans[node].add(node)
                ans[node].add(candidate)
                ans[node].update(ans[candidate])
        for i in ans:
            res[i]=(list(ans[i]))

        for i in range(len(res)):
            mini=float("inf")
            if len(res[i])!=0:
                for j in range(len(res[i])):
                    mini=min(mini,quiet[res[i][j]])

                final.append(quiet.index(mini))
            else:
                final.append(i)

        return (final)


             
        


        

      
