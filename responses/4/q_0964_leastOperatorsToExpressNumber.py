class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = k = 0
        while target > 0:
            target, rem = divmod(target, x)
            if k > 0:
                neg, pos = min(rem * k + neg, (rem + 1) * k + pos), min((x - rem) * k + neg, (x - rem - 1) * k + pos)
            k += 1
        return min(pos, k + neg) - 1
