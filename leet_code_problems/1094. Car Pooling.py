class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        new=0
        
        for i in range(len(trips)):
            new=max(new,trips[i][-1])
            
        prefix=[0 for i in range(new+1)]
        
        for i,j,k in trips:
            prefix[j]+=i
            prefix[k]+=-i
            
        for p in range(1,len(prefix)):
            prefix[p]+=prefix[p-1]
            
        if max(prefix)>capacity:
            return False
        else:
            return True
        #Time Complexity O(n)
        # Space Complexity O(n)
