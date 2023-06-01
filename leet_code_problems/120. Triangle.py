class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = {}
        def min_path(r,c):

            if r == len(triangle)-1:
                return triangle[r][i]
            if (r,i) in memo:
                return memo[(r,i)]
            memo[(r,i)] = triangle[r][i] + min(min_path(r+1,c),min_path(r+1,c+1))
            return memo[(r,c)]

        min_path(0,0)

        return memo[(0,0)] if len(triangle) > 1 else triangle[0][0]

