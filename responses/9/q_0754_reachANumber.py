class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = 1
        total = 0
        while total < target or (total - target) % 2 != 0:
            total += n
            n += 1
        return n - 1
