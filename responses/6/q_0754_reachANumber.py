class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int((-1 + (1 + 8*target)**0.5) / 2)
        s = n * (n + 1) // 2
        if s == target:
            return n
        diff = s - target
        if (diff % 2 == 0):
            return n
        else:
            return n + 1 + n % 2
