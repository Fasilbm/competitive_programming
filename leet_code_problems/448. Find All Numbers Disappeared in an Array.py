class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        while i<len(nums):
            corr=nums[i]-1
            if nums[i]!=nums[corr]:
                nums[i],nums[corr]=nums[corr],nums[i]
            else:
                i+=1
        print(nums)
        for i in range(len(nums)):
            if nums[i]!=i+1:
                ans.append(i+1)

        return ans
