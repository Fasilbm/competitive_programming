# O(n*m) time complexity   0(m) space complexity
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]: 
        k={val:i for i,val in enumerate(nums1)}
        list=[-1]*len(nums1)  
        for i in range (len(nums2)):
            if nums2[i] not in nums1:
                    continue
            for j in  range (i+1,len(nums2)):
                    if nums2[j]>nums2[i]:
                         m=k[nums2[i]]
                         list[m]=nums2[j]
                         break
        return list
                    
           
