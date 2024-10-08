from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = []
        for target in range(n, 1, -1):
            idx = arr.index(target)
            if idx != target - 1:
                if idx != 0:
                    res.append(idx + 1)
                    arr = arr[:idx+1][::-1] + arr[idx+1:]
                res.append(target)
                arr = arr[:target][::-1] + arr[target:]
        return res