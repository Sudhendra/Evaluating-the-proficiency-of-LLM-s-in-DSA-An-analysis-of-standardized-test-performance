from typing import List

class Solution:
    
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], color)
        return image
    
    def fill(self, image, r, c, old_color, new_color):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != old_color:
            return
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        image[r][c] = new_color
        
        for dr, dc in dirs:
            self.fill(image, r + dr, c + dc, old_color, new_color)
