from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        arr = [0] + arr + [0]
        n = len(arr)
        result = 0
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                j = stack.pop()
                result += arr[j] * (i - j) * (j - stack[-1])
            stack.append(i)
        return result % MOD
