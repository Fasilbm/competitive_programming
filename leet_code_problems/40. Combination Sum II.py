class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        
        def backtracking(comb,i,target):

            if sum(comb) == target :
                ans.append(comb.copy())
                return

            if sum(comb)>target :
                return

            if i >= len(candidates):
                return

            comb.append(candidates[i])
            backtracking(comb,i+1,target)
            comb.pop()

            indx = i + 1
            while indx < len(candidates) and candidates[indx] == candidates[i]:
                indx += 1

            backtracking(comb,indx,target)

        backtracking([],0,target)
        return ans

