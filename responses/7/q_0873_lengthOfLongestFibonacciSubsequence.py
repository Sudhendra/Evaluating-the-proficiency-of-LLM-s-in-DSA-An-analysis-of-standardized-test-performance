from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        longest = 0
        n = len(arr)
        s = set(arr)

        for i in range(n):
            for j in range(i + 1, n):
                a, b = arr[i], arr[j]
                l, m, length = 2, a + b, 2

                while m in s:
                    l, m, length = m, l + m, length + 1
                    longest = max(longest, length)

        return longest if longest > 2 else 0
