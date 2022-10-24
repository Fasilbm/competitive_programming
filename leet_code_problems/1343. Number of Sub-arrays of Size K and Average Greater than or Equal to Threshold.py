class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start=0
        cur=0
        count=0
        for i in range(len(arr)):
            cur+=arr[i]
            while i-start==k-1:
                if (cur/k)>=threshold:
                       count+=1
                cur-=arr[start]
                start+=1
        return count
    # Time Complexity O(n)
    # Space Complexity O(1)
    
        
                      
