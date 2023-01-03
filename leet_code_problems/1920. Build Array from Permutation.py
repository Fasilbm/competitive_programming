class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        perm=[0]*len(nums)
        for i in range (len(nums)):
            perm[i]=nums[nums[i]]
        return perm
            
        
