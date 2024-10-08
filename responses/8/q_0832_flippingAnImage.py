from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1 ^ pixel for pixel in reversed(row)] for row in image]
