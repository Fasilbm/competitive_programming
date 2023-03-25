class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i,j in enumerate(nums):
            if j==count and i==len(nums)-1:
                return count+1
            elif j==count:
                count+=1
            else:
                return count
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        checker=[]
        for i in range(len(nums)+1):
            checker.append(i)
            
        for i in checker:
            if i not in nums:
                return i
class Solution:
        def missingNumber(self, nums: List[int]) -> int:

            i=0
            while i<len(nums):
                corr = nums[i]
                if i!=corr and corr!=len(nums):
                    nums[corr],nums[i]=nums[i],nums[corr]
                else:
                    i+=1
            for i in range(len(nums)):
                if nums[i]!=i:
                    return i

            return len(nums)



            


            


        


