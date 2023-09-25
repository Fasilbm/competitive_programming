class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        pair = []
        for i in range(len(scores)):
            pair.append((scores[i],ages[i]))

        pair = sorted(pair, key=lambda x:(x[1], x[0]),reverse = True)
        ans = 1 
        @cache
        def find(i):
            if i == len(pair)-1:
                return pair[i][0]
            curr = pair[i][0]
            for j in range(i+1, len(pair)):
                if pair[i][0] >= pair[j][0]:
                    score = find(j)
                    curr = max(pair[i][0] + score, curr)

            return curr
            
        for i in range(len(pair)):
            ans=max(ans,find(i))
        return ans
