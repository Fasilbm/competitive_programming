class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        list=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
        for k in range (len(nums)):
            if target==nums[k]:
                 list.append(k)
        return list
           
