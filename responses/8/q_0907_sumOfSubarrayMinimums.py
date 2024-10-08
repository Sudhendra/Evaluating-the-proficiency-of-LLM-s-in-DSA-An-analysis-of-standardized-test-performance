from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        arr = [0] + arr + [0]
        result = 0
        n = len(arr)
        
        left = [0] * n
        right = [0] * n
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                top = stack.pop()
                right[top] = i
            stack.append(i)
        
        stack = []
        
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                left[top] = i
            stack.append(i)
        
        for i in range(1, n-1):
            result += arr[i] * (i - left[i]) * (right[i] - i)
            result %= MOD
        
        return result

# Test cases
solution = Solution()
print(solution.sumSubarrayMins([3,1,2,4]))  # Output: 17
print(solution.sumSubarrayMins([11,81,94,43,3]))  # Output: 444
