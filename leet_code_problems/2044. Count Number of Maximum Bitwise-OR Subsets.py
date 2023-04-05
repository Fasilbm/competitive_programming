class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
    
        maximum_or=0
        for i in nums:
            maximum_or=(maximum_or|i)
        ans=[]

        def dfs(maximum_or,i,comb):
            if i>=len(nums):
                return
            comb.append(nums[i]) 
            b=0
            for x in comb:
                b|=x
            if b==maximum_or:
                ans.append(comb.copy())
           
            dfs(maximum_or,i+1,comb)
            comb.pop()
            dfs(maximum_or,i+1,comb)

        dfs(maximum_or,0,[])

        return len(ans)


