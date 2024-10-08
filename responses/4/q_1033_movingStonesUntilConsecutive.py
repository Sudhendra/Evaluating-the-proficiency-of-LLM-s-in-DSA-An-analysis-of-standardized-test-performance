from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()

        min_moves = 2  # Minimum number of moves is always 2
        if stones[2] - stones[0] == 2:
            min_moves = 0  # Max 2 moves can be achieved when 3 stones are consecutive
        elif stones[1] - stones[0] <= 2 or stones[2] - stones[1] <= 2:
            min_moves = 1  # Only 1 move needed to make stones consecutive

        max_moves = stones[2] - stones[0] - 2  # Maximum moves is the range between the stones minus 2

        return [min_moves, max_moves]
