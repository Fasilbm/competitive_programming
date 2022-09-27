class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr=0
        count=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[i],nums[ptr]=nums[ptr],nums[i]
                ptr+=1
            else:
                count+=1
        while len(nums)>1 and count>0:
            nums.pop()
        return len(nums)
    
    
    
        
            
