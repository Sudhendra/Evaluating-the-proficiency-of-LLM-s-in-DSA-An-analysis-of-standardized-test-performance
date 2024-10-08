class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        arr = [0] + arr + [0]
        for i, x in enumerate(arr):
            while stack and arr[stack[-1]] > x:
                j = stack.pop()
                k = stack[-1]
                result = (result + arr[j] * (i - j) * (j - k)) % MOD
            stack.append(i)
        return result
