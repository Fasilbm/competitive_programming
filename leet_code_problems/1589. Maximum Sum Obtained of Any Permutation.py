class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:       
        prefix=[0]*(len(nums)+1)
        for i,j in requests:

            prefix[i]+=1
            prefix[j+1]-=1
        
        for i in range(1,len(prefix)):

            prefix[i]+=prefix[i-1]

        prefix=prefix[:len(prefix)-1]
        count={i:n for i,n in enumerate(prefix)}
        new=[0]*len(nums)
        nums.sort()
        count={k: v for k, v in sorted(count.items(), key=lambda item: -item[1])}
        new=[]
        for i in count.items():
            new.append(i)

        changed=[0]*len(nums)

        for i,j in new:

            changed[i]=nums[-1]
            nums.pop() 
        ans=0
        for i in range(1,len(changed)):

            changed[i]+=changed[i-1]

        Sum=0
        for i,j in requests:

            if i!=0:
                Sum += changed[j]-changed[i-1]
            else:
                Sum += changed[j]

        return Sum % ((10**9)+7)

        



        


