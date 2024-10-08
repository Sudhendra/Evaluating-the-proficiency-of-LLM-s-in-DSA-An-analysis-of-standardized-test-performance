from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, indices, counts):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = mergeSort(arr[:mid], indices, counts)
            right = mergeSort(arr[mid:], indices, counts)
            merged = []
            i = j = 0
            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                    indices[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged

        indices = [0] * len(nums)
        mergeSort(list(enumerate(nums)), indices, [0] * len(nums))
        return indices
