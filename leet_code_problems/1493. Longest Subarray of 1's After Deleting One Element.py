class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        start=0
        res=0
        for i in range(len(nums)):
            if nums[i]==1:
                res=max(res,i-start)
                continue
            if nums[i]==0:
                count+=1
                while count>1 and start<len(nums):
                    if nums[start]==0:
                        count-=1
                    start+=1
            res=max(res,i-start)
        return res
    
    # Time Complexity O(n)
    # Space Complexity O(1)
