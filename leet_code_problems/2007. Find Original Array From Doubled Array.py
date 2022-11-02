class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n=len(changed)
        if n%2:
             return ([])
        ans=[]
        count=Counter(changed)
        changed.sort()
        for i in changed:
            if i==0 and count[0]>=2:
                count[0]-=2
                ans.append(i)
            elif i!=0 and count[i] and count[i*2]:
                ans.append(i)
                count[i]-=1
                count[i*2]-=1
        if len(ans)==n//2:
            return (ans)
        else:
            return ([])
