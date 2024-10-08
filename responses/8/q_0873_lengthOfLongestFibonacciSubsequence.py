from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        max_length = 0
        possible_sequences = {}

        for i in range(len(arr)):
            for j in range(i):
                x, y = arr[j], arr[i]
                if x < y:
                    z = x + y
                    cur_length = 2
                    while z in possible_sequences:
                        x, y = y, z
                        z = x + y
                        cur_length += 1
                    max_length = max(max_length, cur_length)
                    possible_sequences[(x, y)] = cur_length

        return max_length
