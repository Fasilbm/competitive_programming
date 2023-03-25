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
            


        


