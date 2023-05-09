class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph=defaultdict(str)
        indegree=defaultdict(int)
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]]=[]
        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                graph[ingredients[i][j]].append(recipes[i])
                indegree[recipes[i]]+=1

        queue=deque(supplies)
        ans=[]
        while queue:
            candidate=queue.popleft()
            ans.append(candidate)
            for node in graph[candidate]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
        res=[]
        for i in ans:
            if i in recipes:
                res.append(i)
        return res

