class Solution:
    def rob(self, nums: List[int]) -> int:

        memo={}

        def find(n):

            if n < 0 :
                return 0

            if n == 0:
                memo[0] = nums[0]
                return memo[0]
            
            if n in memo:
                return memo[n]

            memo[n] = max(find(n-2) + nums[n],find(n-1))

            return memo[n]

        x=find(len(nums)-2)
        
        memo={}
        def find1(n):
            if n < 1 :
                return 0

            if n == 1:
                memo[1] = nums[1]
                return memo[1]
            
            if n in memo:
                return memo[n]

            memo[n] = max(find1(n-2) + nums[n],find1(n-1))

            return memo[n]

        y=find1(len(nums)-1)

        return max(x,y) if len(nums)>1 else nums[0]
