class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        def backtrack(inital,cur):

            if len(cur) == k :
                ans.append(cur.copy())

            for candidate in range(inital,n+1):
                cur.append(candidate)
                backtrack(candidate+1,cur)
                cur.pop()

        backtrack(1,[])

        return ans
            





