class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        left1=len(nums)-1
        left2=len(nums)-2
        left3=len(nums)-3
        while left3>=0:
            if nums[left3]+nums[left2]>nums[left1]:
                return nums[left1]+nums[left2]+nums[left3]
            else:
                left1-=1
                left2-=1
                left3-=1
        return 0
            
   

            
