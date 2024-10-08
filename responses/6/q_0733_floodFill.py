from typing import List

class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def dfs(image, r, c, color, new_color):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != color or image[r][c] == new_color:
                return
            image[r][c] = new_color
            dfs(image, r+1, c, color, new_color)
            dfs(image, r-1, c, color, new_color)
            dfs(image, r, c+1, color, new_color)
            dfs(image, r, c-1, color, new_color)

        if image[sr][sc] == color:
            return image
        dfs(image, sr, sc, image[sr][sc], color)
        return image
