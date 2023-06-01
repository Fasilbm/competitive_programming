class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def find(amount):

            if amount == 0:
                return 0

            if amount < 0 :
                return float("inf")
                
            if amount in memo:
                return memo[amount]

            best = float("inf")
            for coin in coins:
                best = min(find(amount-coin),best)
            memo[amount] = best + 1

            return memo[amount]


        res = find(amount)

        return -1 if res == float("inf") else res
            
      



