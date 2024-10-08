class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        steps = 0
        current_sum = 0
        while current_sum < target or (current_sum - target) % 2 != 0:
            steps += 1
            current_sum += steps
        return steps