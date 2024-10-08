class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()
        
        min_moves = 0
        max_moves = (stones[2] - stones[1] - 1) + (stones[1] - stones[0] - 1)
        
        # Calculate min_moves by moving one endpoint to the midpoint
        if stones[2] - stones[1] > 1 and stones[1] - stones[0] > 1:
            min_moves = min(stones[1] - stones[0], stones[2] - stones[1]) <= 2
        elif stones[1] - stones[0] > 2 or stones[2] - stones[1] > 2:
            min_moves = 1
        
        return [min_moves, max_moves]
