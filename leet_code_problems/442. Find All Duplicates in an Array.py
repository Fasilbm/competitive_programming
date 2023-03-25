class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        
        ans=[]
        i=0
        while i<len(nums):
            corr=nums[i]-1
            if nums[i]!=nums[corr]:
                nums[i],nums[corr]=nums[corr],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if i!=nums[i]-1:
                ans.append(nums[i])
        return ans



