class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = 0
        total = 0
        while total < target or (total - target) % 2 != 0:
            n += 1
            total += n
        return n
