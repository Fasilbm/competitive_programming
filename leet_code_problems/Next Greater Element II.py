class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        out=[-1]*len(nums)
        dic={}
        for i,n in enumerate(nums):
            dic[n]=i
        head=0
        tail=1
        if len(nums)==1: return out
        for i in nums: 
            
            while (head!=tail):
                if nums[head]<nums[tail]:
                    k=dic[nums[head]]
                    out[k]=nums[tail]
                    head=(head+1) % len(nums)
                    tail=(tail+1) % len(nums)
                    break
                else:
                    tail=(tail+1) % len(nums)
            if head==tail:
                head=(head+1)%len(nums)
                tail=(tail+2)%len(nums)
                
            
        return out
