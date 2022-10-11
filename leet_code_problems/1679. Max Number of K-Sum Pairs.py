class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        l=0
        r=len(nums)-1
        nums.sort()
        while r>l:
            if nums[l]+nums[r]>k:
                r-=1
            elif nums[l]+nums[r]<k:
                l+=1
            else:
                count+=1
                l+=1
                r-=1
        return count
    # Time complexity O(nlogn)
    # Space complexity O(1)
