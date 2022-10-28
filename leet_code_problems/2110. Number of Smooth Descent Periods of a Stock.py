class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans=[]
        l,r=0,0
        while l<len(prices) and r<len(prices):
            if l==r:
                ans.append(1)
                r+=1
            elif prices[r-1]-prices[r]==1:
                ans.append(r-l+1)
                r+=1
            else:
                l=r
        return sum(ans)
        
        # Time Complexity O(n)
        # Space Complexity O(n)
            
            
