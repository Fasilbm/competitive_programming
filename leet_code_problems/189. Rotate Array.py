class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        
        nums[:]=nums[len(nums)-k:]+nums[0:len(nums)-k]
        # Time complexity O(n)
        # space complexity O(1)
        
    
