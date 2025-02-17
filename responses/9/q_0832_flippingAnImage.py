from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            image[i] = image[i][::-1]  # Reverse each row
            for j in range(n):
                image[i][j] = 1 - image[i][j]  # Invert the image
        return image
