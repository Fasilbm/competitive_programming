class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict={0:1}
        curr=0
        res=0
        for i in nums:
            curr+=i
            modu=curr%k
            res+=dict.get(modu,0)
            dict[modu]=1+dict.get(modu,0)
        return res
    # Time Complexity O(n)
    # space complexity O(1)
    
   
    
