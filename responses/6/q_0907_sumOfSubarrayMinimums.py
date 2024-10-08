from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr = [0] + arr + [0]
        n = len(arr)
        dp = [1] * n

        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                dp[j] = i - j

            stack.append(i)

        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            left = stack[-1]
            right = i
            result = (result + arr[i] * dp[i] * (i - left) * (right - i)) % MOD
            stack.append(i)

        return result
