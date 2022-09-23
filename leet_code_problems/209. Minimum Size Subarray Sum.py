class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        curr_sum=0
        res=len(nums)+1
        for i in range(len(nums)):
            curr_sum+=nums[i]
            while curr_sum>=target:
                res=min(i-start+1,res)
                curr_sum-=nums[start]
                start+=1
        return res if res<len(nums)+1 else 0
    # Time complexity O(n)
    # Space complexity O(1)
                
            
