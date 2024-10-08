from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image or color == image[sr][sc]:
            return image

        def dfs(image, sr, sc, color, new_color):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color:
                return
            image[sr][sc] = new_color
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                dfs(image, sr + dx, sc + dy, color, new_color)

        dfs(image, sr, sc, image[sr][sc], color)
        return image
