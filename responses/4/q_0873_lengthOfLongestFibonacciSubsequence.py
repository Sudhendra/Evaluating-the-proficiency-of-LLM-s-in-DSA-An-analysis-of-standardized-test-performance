from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        num_set = set(arr)
        n = len(arr)
        max_length = 0

        for i in range(n):
            for j in range(i + 1, n):
                a, b, length = arr[i], arr[j], 2
                while a + b in num_set:
                    a, b = b, a + b
                    length += 1
                max_length = max(max_length, length)

        return max_length if max_length > 2 else 0
