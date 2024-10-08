class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            arr[:k] = arr[:k][::-1]
        
        n = len(arr)
        res = []
        for x in range(n, 1, -1):
            idx = arr.index(x)
            if idx == x - 1:
                continue
            if idx != 0:
                flip(arr, idx + 1)
                res.append(idx + 1)
            flip(arr, x)
            res.append(x)
        return res
