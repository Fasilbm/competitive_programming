class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        phash=Counter(p)
        shash=Counter(s[0:len(p)])
        res=[0] if phash==shash else []
        if len(s)<len(p): return []
        l=0
        for i in range(len(p),len(s)):
            shash[s[i]]=1+shash.get(s[i],0)
            shash[s[l]]-=1
            l+=1
            if shash==phash:
                res.append(l)
        return res
    
    # Time Complexity O(26*n)
    # space complexity O(1)
