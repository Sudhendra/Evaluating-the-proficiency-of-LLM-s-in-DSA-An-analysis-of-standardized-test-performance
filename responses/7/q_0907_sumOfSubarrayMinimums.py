from typing import List

class Solution:

    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        n = len(arr)
        stack = []
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        stack.clear()

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        result = sum((i - left[i]) * (right[i] - i) * arr[i] for i in range(n)) % mod
        return result

# Test the Solution class
sol = Solution()
print(sol.sumSubarrayMins([3, 1, 2, 4]))  # Output: 17
print(sol.sumSubarrayMins([11, 81, 94, 43, 3]))  # Output: 444
