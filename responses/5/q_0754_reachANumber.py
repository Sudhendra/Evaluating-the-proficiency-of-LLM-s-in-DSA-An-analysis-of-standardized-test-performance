class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = int(((1 + 8 * target) ** 0.5 - 1) / 2)
        if target % 2 == 0:
            while n % 4 != 0:
                n += 1
        else:
            while n % 2 != 0:
                n += 1
        return n
