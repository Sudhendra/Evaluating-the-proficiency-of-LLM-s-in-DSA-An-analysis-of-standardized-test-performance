from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            else:
                mid = len(arr) // 2
                left, cnt_left = merge_sort(arr[:mid])
                right, cnt_right = merge_sort(arr[mid:])
                cnt = cnt_left + cnt_right
                
                j = 0
                for num in left:
                    while j < len(right) and num > 2 * right[j]:
                        j += 1
                    cnt += j
                
                return list(sorted(left + right)), cnt

        _, result = merge_sort(nums)
        return result
