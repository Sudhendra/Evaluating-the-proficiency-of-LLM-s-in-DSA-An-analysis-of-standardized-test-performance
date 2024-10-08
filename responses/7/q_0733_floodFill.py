from typing import List

class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image

        def dfs(r, c):
            if (not (0 <= r < len(image) and 0 <= c < len(image[0])) or image[r][c] != originalColor):
                return
            image[r][c] = newColor
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        originalColor = image[sr][sc]
        dfs(sr, sc)

        return image
