from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        n = len(arr)
        target = n

        for i in range(n):
            max_index = arr.index(target)
            result.extend([max_index + 1, target])
            arr = arr[:max_index + 1][::-1] + arr[max_index + 1:]

            max_index = arr.index(target - 1)
            result.extend([max_index + 1, target - 1])
            arr = arr[:max_index + 1][::-1] + arr[max_index + 1:]

            target -= 1

        return result
