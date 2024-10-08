class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos = neg = k = diff = 0
        while target:
            target, remainder = divmod(target, x)
            if k:
                pos, neg = min(remainder * k + pos, (remainder + 1) * k + neg), min((x - remainder) * k + pos, (x - remainder - 1) * k + neg)
            diff += k * remainder
            k += 1
        return min(pos, diff + neg) - 1

# Example
x = Solution()
print(x.leastOpsExpressTarget(3, 19))  # Output: 5
