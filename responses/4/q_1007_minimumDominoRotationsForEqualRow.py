from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x: int) -> int:
            top_rotations = 0
            bottom_rotations = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    top_rotations += 1
                elif bottoms[i] != x:
                    bottom_rotations += 1
            return min(top_rotations, bottom_rotations)

        rotations = check(tops[0])  # Check if it's possible to make all tops match tops[0]
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return check(bottoms[0])  # Check if it's possible to make all tops match bottoms[0]

# Example usage:
# solution = Solution()
# print(solution.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))  # Output: 2
# print(solution.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))  # Output: -1
