class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        pre_mul=[1]
        post_mul=[1]*(len(nums)+1)
        ans=[]

        for i in range(len(nums)):

            pre_mul.append(pre_mul[-1]*nums[i])

        for j in range(len(nums)-1,-1,-1):

            post_mul[j]=post_mul[j+1]*nums[j]

        # print(pre_mul)
        # print(post_mul)

        for i in range(len(nums)):

                ans.append(post_mul[i+1]*pre_mul[i])

        return (ans)
