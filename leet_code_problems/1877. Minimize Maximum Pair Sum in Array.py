class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        stack=[]
        nums.sort()
        while l<r:
            stack.append(nums[l]+nums[r])
            l+=1
            r-=1
        return max(stack)
    # Time Complexity O(nlogn)
    # Space complexity O(n)
