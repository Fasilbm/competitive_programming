class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        def backtracking(comb,i,target):
            if sum(comb) == target :
                ans.append(comb.copy())
                return

            if sum(comb) > target:
                return
            
            if i >= len(candidates):   
                return

            comb.append(candidates[i])
            backtracking(comb,i,target)
            comb.pop()
            backtracking(comb,i+1,target)
             

        backtracking([],0,target)

        return ans

            



       

                
