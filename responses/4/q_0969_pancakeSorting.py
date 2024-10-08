from typing import List

class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []

        def flip(subarr_end):
            nonlocal arr, flips
            left, right = 0, subarr_end
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            flips.append(subarr_end + 1)

        n = len(arr)
        for target in range(n, 1, -1):
            idx = arr.index(target)
            if idx != target - 1:
                if idx != 0:
                    flip(idx)  # First flip to move the target to front
                flip(target - 1)  # Second flip to move the target to correct position

        return flips
