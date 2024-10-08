class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = k = 0
        while target:
            target, remainder = divmod(target, x)
            if k > 0:
                pos, neg = min(remainder * k + pos, (remainder + 1) * k + neg), min((x - remainder) * k + pos, (x - remainder - 1) * k + neg)
            else:
                pos, neg = x * remainder, x * (x - remainder)
            k += 1
        return min(pos, k + neg) - 1
