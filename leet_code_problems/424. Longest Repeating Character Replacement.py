class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        l=0 
        r=0
        res=0
        while r<len(s):
            count[s[r]]+=1
            freq=max(count.values())
            if (r-l+1)-freq<=k:
                res=max(res,r-l+1)
                r+=1
            else:
                count[s[l]]-=1
                count[s[r]]-=1

                l+=1
        return res
        # Time complexity O(n)
        # Space Complexity O(1)
