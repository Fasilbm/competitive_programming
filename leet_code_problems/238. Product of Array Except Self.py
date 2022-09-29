class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[0 for i in range(len(nums))]
        prefix=[0 for i in range(len(nums))]
        postfix=[0 for i in range(len(nums))]
        prefix[0]=nums[0]
        postfix[len(nums)-1]=nums[len(nums)-1]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i]
            prefix.append(prefix[i])
        for i in range(len(nums)-2,-1,-1):
            postfix[i]=nums[i]*postfix[i+1]
            postfix.append(postfix[i])
        result[0]=postfix[1]
        result[len(nums)-1]=prefix[len(nums)-2]
        for j in range(1,len(nums)-1):
            result[j]=prefix[j-1]*postfix[j+1]
        return result
    #Time complexity O(n)
    #Space complexity O(n)
