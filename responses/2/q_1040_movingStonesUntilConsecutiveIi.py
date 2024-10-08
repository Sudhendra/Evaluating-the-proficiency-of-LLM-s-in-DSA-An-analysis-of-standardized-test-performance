class Solution:
    
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        
        max_moves = max(stones[-2] - stones[0] - n + 2, stones[-1] - stones[1] - n + 2)
        
        min_moves = n
        left = 0
        for right in range(n):
            while stones[right] - stones[left] >= n:
                left += 1
            if right - left + 1 == n - 1 and stones[right] - stones[left] == n - 2:
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - (right - left + 1))
        
        return [min_moves, max_moves]
