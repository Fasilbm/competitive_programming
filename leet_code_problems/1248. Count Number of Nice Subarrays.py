class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr=0
        ans=0
        hashmap={0:1}
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1

        for i in nums:
            curr+=i
            diff=curr-k
            ans+=hashmap.get(diff,0)
            hashmap[curr]=1+hashmap.get(curr,0)
            
        return ans
    # Time Complexity O(n)
    # Space Complexity O(1)
        
      
