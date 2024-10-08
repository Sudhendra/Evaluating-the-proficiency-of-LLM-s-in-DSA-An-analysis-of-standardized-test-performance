from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for i in range(n, 1, -1):
            idx = arr.index(i)
            if idx == i - 1:
                continue
            if idx != 0:
                res.append(idx + 1)
                arr = arr[:idx+1][::-1] + arr[idx+1:]
            res.append(i)
            arr = arr[:i][::-1] + arr[i:]
        return res
