class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        cost.append(0)
        def step(n):
            if n in memo: return memo[n]
            if n<0:
                return 0
            if n==0:
                memo[n] = cost[0]
                return memo[n]
            memo[n] = (cost[n])+ min(step(n-1),step(n-2))

            return memo[n]

        return step(len(cost)-1)
            
        

        
