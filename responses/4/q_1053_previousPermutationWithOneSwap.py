from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        idx = -1

        # Find the rightmost index where arr[i] > arr[i+1]
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                idx = i
                break

        if idx == -1:
            return arr

        # Find the rightmost index where arr[j] < arr[i]
        for j in range(n - 1, idx, -1):
            if arr[j] < arr[idx] and arr[j] != arr[j - 1]:
                arr[j], arr[idx] = arr[idx], arr[j]
                return arr

        return arr
