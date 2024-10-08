from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            arr[:k] = arr[:k][::-1]
        
        n = len(arr)
        res = []
        target = n
        
        for target in range(n, 0, -1):
            idx = arr.index(target)
            if idx == target - 1:
                continue
            if idx != 0:
                res.append(idx + 1)
                flip(arr, idx + 1)
            res.append(target)
            flip(arr, target)
        
        return res
