class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=len(nums1)-1
        for i in range(n-1,-1,-1):
            nums1[l]=nums2[i]
            l-=1
        return nums1.sort()
      

