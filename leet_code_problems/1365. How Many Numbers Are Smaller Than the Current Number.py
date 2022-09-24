class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result=[]
        dic={}
        original=nums.copy()
        for i in range(len(nums)):
            mini=i
            for j in range(i+1,len(nums)):
                if nums[mini]>nums[j]:
                    mini=j
            nums[mini],nums[i]=nums[i],nums[mini]
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=i
        for i in original:
            result.append(dic[i])
        return result
    # time complexity O(n^2)
    # space complexity O(n)
    
                    
        
    
                       
        
        
            
