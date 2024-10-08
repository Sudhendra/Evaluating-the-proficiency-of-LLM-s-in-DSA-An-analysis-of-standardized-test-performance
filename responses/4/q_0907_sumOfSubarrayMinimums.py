from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        prev_smaller = [None] * len(arr)
        next_smaller = [None] * len(arr)
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                top = stack.pop()
                next_smaller[top] = i
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        result = 0
        for i in range(len(arr)):
            prev_dist = i - prev_smaller[i] if prev_smaller[i] is not None else i + 1
            next_dist = next_smaller[i] - i if next_smaller[i] is not None else len(arr) - i
            result += arr[i] * prev_dist * next_dist
            result %= MOD
        return result
