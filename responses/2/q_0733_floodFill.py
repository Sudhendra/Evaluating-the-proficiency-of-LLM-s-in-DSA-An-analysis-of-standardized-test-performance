from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or image[sr][sc] == newColor:
            return image
        
        def dfs(image, sr, sc, color, newColor):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != color:
                return
            image[sr][sc] = newColor
            dfs(image, sr+1, sc, color, newColor)
            dfs(image, sr-1, sc, color, newColor)
            dfs(image, sr, sc+1, color, newColor)
            dfs(image, sr, sc-1, color, newColor)
        
        color = image[sr][sc]
        dfs(image, sr, sc, color, newColor)
        return image
