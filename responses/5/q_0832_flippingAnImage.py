from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            left, right = 0, n - 1
            while left <= right:
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                left += 1
                right -= 1
        return image
