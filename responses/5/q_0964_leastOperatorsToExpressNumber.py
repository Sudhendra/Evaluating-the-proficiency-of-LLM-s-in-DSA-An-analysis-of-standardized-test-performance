class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = k = msb = 0
        while target:
            target, remainder = divmod(target, x)
            if k > 0:
                pos, neg = min(remainder * k + neg, (x - remainder) * k + pos), min(remainder * k + neg + k, (x - remainder) * k + pos + k)
            k, msb = k + 1, remainder
        return min(pos, k + neg) - 1
