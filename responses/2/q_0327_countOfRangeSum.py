from sortedcontainers import SortedList
from bisect import bisect_left, bisect_right

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        def merge_sort(lo, hi):
            if (hi - lo) <= 1:
                return 0
            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            i = j = mid
            for left in prefix_sum[lo:mid]:
                while i < hi and prefix_sum[i] - left < lower:
                    i += 1
                while j < hi and prefix_sum[j] - left <= upper:
                    j += 1
                count += j - i
            prefix_sum[lo:hi] = sorted(prefix_sum[lo:hi])
            return count
        
        return merge_sort(0, len(prefix_sum))
