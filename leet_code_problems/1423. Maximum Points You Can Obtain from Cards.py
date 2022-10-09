class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l,r=0,len(cardPoints)-k
        total=sum(cardPoints[r:])
        res=total
        for i in range(r,len(cardPoints)):
            total+=cardPoints[l]-cardPoints[i]
            res=max(res,total)
            l+=1
        return res
    # Time Complexity O(k)
    # Space complexityO(1)
