class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        curr_sum = 0
        num_moves = 0
        while curr_sum < target or (curr_sum - target) % 2 != 0:
            num_moves += 1
            curr_sum += num_moves
        return num_moves
