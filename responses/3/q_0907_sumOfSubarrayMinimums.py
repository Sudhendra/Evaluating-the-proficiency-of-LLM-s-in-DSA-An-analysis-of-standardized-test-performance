class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        ans = 0
        arr = [0] + arr + [0]
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                middle = stack.pop()
                left = stack[-1]
                right = i
                ans += arr[middle] * (right - i) * (middle - left)
            stack.append(i)
        return ans % MOD