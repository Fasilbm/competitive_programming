class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cur_sum=0
        max_sum=float("-inf")
        start=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            while i-start+1==k:
               max_sum=max(cur_sum,max_sum)
               cur_sum-=nums[start]
               start+=1
            

        return max_sum/k
            






