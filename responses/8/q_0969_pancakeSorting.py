from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        for x in range(n, 1, -1):
            i = arr.index(x)
            if i != x - 1:
                if i != 0:
                    res.append(i + 1)
                    arr = arr[:i+1][::-1] + arr[i+1:]
                res.append(x)
                arr = arr[:x][::-1] + arr[x:]

        return res
