class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        k={}
        for i,val in enumerate(nums1):
            k[val]=i
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
        
        # O(m+n) Time O(m) Space
        k={}
        for i,val in enumerate(nums1):
            k[val]=i
        list=[-1]*len(nums1) 
        stack=[]
        for i in range (len(nums2)):
            curr=nums2[i]
            while stack and curr >stack[-1]:
                val=stack.pop()
                m=k[val]
                list[m]=curr
            if curr in nums1:
                stack.append(curr)
        return list  
                
