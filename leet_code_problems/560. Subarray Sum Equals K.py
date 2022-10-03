class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        sum=0
        res=0
        for i in nums:
            sum+=i
            diff=sum-k
            res+=dic.get(diff,0)
            dic[sum]=1+dic.get(sum,0)
        return res
       #Time complexity O(n)
       #Space complexity O(1)
