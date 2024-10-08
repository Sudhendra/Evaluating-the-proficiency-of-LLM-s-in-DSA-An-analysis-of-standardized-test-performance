from typing import List

class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]:
        if not image or image[sr][sc] == color:
            return image

        def dfs(image, sr, sc, color, initial_color):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != initial_color:
                return
            image[sr][sc] = color
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(image, sr + dr, sc + dc, color, initial_color)

        initial_color = image[sr][sc]
        dfs(image, sr, sc, color, initial_color)
        return image
