from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        for x in range(n, 1, -1):
            i = arr.index(x)
            if i != x - 1:
                result.extend([i + 1, x])
                arr = arr[:i+1][::-1] + arr[i+1:]
                arr = arr[:x][::-1] + arr[x:]
        return result