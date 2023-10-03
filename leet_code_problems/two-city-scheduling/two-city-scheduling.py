class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key = lambda x:x[0]-x[1])
        n = len(costs)//2
        cost=0
        
        for i in range(n):
            cost += costs[i][0]
           
        for i in range(len(costs)-1,n-1,-1):
            cost += costs[i][1]
          
        return cost
            



