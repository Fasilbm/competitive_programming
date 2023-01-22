class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        nums.sort()
        for i,j in enumerate(nums):
            if j==target:
                ans.append(i)
        return ans
