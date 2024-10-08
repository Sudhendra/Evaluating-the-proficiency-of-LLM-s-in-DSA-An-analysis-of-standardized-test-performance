from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        n = len(arr)
        max_len = 0

        for i in range(n):
            for j in range(i+1, n):
                a, b = arr[i], arr[j]
                cur_len = 2

                while a + b in s:
                    a, b = b, a + b
                    cur_len += 1

                max_len = max(max_len, cur_len)

        return max_len if max_len >= 3 else 0
