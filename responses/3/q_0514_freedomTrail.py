class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        memo = {}

        def dp(pos, index):
            if index == m:
                return 0
            if (pos, index) in memo:
                return memo[(pos, index)]

            result = float('inf')
            for i in range(n):
                if ring[i] == key[index]:
                    clock = abs(i - pos)
                    anticlock = n - clock
                    steps = min(clock, anticlock) + 1
                    next_steps = steps + dp(i, index + 1)
                    result = min(result, next_steps)

            memo[(pos, index)] = result
            return result

        return dp(0, 0)
