from sortedcontainers import SortedList
from bisect import bisect_left, bisect_right

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def countAndMergeSort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = countAndMergeSort(lo, mid) + countAndMergeSort(mid, hi)
            j = k = t = mid
            merged = []
            for i in range(lo, mid):
                while k < hi and prefix_sum[k] < prefix_sum[i]:
                    merged.append(prefix_sum[k])
                    k += 1
                while j < hi and prefix_sum[j] - prefix_sum[i] < lower:
                    j += 1
                while t < hi and prefix_sum[t] - prefix_sum[i] <= upper:
                    t += 1
                count += t - j
                merged.append(prefix_sum[i])

            merged += prefix_sum[k:hi]
            prefix_sum[lo:hi] = merged
            return count

        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        return countAndMergeSort(0, len(prefix_sum))

    # If you have multiple solutions, add them all here as methods of the same class.
