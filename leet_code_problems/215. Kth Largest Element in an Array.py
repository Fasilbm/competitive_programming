class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        target=len(nums)-k

        def quickselect(start,end):
            pivot=nums[start]
            write=start+1
            for read in range(start+1,end+1):
               if nums[read]<pivot:
                   nums[write],nums[read]=nums[read],nums[write]
                   write+=1
            nums[start],nums[write-1]=nums[write-1],nums[start]
            
            if target==write-1:
                return nums[write-1]
            elif target>write-1:
                return quickselect(write,end)
            else:
                return quickselect(start,write-1)

        return quickselect(0,len(nums)-1)
