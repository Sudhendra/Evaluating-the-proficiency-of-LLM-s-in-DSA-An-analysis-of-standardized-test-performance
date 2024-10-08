class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        pos_power, neg_power = [], []
        power, val = 1, x
        while val < target:
            pos_power.append((val - target, val, power))
            neg_power.append((val - target, val, power))
            power += 1
            val *= x
        pos_power.append((val - target, val, power))
        neg_power.append((val - target, val, power))

        def min_ops(lst):
            dp = [float('inf')] * len(lst)
            for idx in range(len(lst) - 1, -1, -1):
                diff, v, p = lst[idx]
                if diff == 0:
                    dp[idx] = 0
                else:
                    k = diff // v
                    left = diff - k * v
                    right = (k + 1) * v
                    dp[idx] = min(k * p + (dp[idx + 1] if idx < len(lst) - 1 else 0),
                                  (k + 1) * p + (dp[idx + 1] if idx < len(lst) - 1 else 0)) + min(left, right)
            return dp[0]

        return min(min_ops(pos_power), len(neg_power) - 1 + pos_power[-1][2])
