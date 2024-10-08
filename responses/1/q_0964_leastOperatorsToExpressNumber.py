class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = k = cost1 = 0

        while target:
            target, remainder = divmod(target, x)
            if k > 0:
                cost2 = min(remainder * k + pos, (x - remainder) * k + neg)
                pos, neg = cost2 + cost1, min(remainder * (k + 1) + neg, (x - remainder) * (k + 1) + pos)
                cost1 = cost2
            else:
                pos, neg = x * remainder, x * (x - remainder)
                cost1 = neg
            k += 1

        return min(pos, k + neg) - 1
