class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l=0
        r=len(tokens)-1
        res=0
        score=0
        while l<=r:
            if tokens[l]<=power:
                score+=1
                power=power-tokens[l]
                l+=1
                res=max(score,res)
            elif tokens[l]>power and score>0:
                power=tokens[r]+power
                score-=1
                r-=1
                res=max(score,res)
            else:
                break
        return res
    # Time Complexity O(nlog n)
    # Space Complexity O(n)
                
