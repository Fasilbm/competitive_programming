class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]
        def backtracking(i,curr_path):
            if i>len(nums)-1:
                return
            if i <= len(nums)-1:
                curr_path.append(nums[i])
                ans.append(curr_path.copy())
            backtracking(i+1,curr_path)
            curr_path.pop()
            backtracking(i+1,curr_path)
            
        backtracking(0,[])

        return ans
