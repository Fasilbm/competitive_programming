class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix={0:1}
        cur=0
        count=0

        for i in nums:

            cur+=i

            diff=cur-goal
            
            if diff in prefix:

                count += prefix[diff]
                
            prefix[cur]=1+prefix.get(cur,0)
            
        return count









