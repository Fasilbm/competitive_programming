class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = [[0 for i in range(len(image[0]))] for j in range(len(image))]
            inbound= lambda row,col: 0 <= row < len(image) and 0 <= col < len(image[0])
            def dfs(image, visited, row, col,color):
                # base case
                visited[row][col] = True
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if inbound(new_row, new_col) and not visited[new_row][new_col]:
                        if image[new_row][new_col]==image[sr][sc]:
                            image[new_row][new_col]=color
                            dfs(image, visited, new_row, new_col,color)
                            
            dfs(image, visited, sr, sc,color)
            image[sr][sc]=color

            return image
