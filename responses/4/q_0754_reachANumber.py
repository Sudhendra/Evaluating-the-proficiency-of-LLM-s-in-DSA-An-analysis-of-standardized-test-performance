class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sum_val = 0
        num_moves = 0
        while sum_val < target:
            num_moves += 1
            sum_val += num_moves
        diff = sum_val - target
        if diff % 2 == 0:
            return num_moves
        else:
            num_moves += 1 if num_moves % 2 == 0 else 2
            return num_moves
