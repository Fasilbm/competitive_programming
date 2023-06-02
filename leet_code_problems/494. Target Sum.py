class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo={}
        def find(n,path_sum):
            if n == len(nums):
                if path_sum == target:
                    return 1
                return 0
            if (n,path_sum) in memo:
                return memo[(n,path_sum)]
        
            memo[(n,path_sum)] = (find(n+1,path_sum + nums[n]) +find(n+1,path_sum - nums[n]))

            return memo[(n,path_sum)]
        return find(0,0)
            


