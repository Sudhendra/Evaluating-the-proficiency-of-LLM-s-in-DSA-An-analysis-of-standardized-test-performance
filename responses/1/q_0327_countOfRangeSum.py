from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(lo, hi):
            if lo == hi:
                return 0
            mid = (lo + hi) // 2
            count = merge_sort(lo, mid) + merge_sort(mid + 1, hi)
            i = j = mid + 1
            for left in prefix_sum[lo:mid+1]:
                while i <= hi and prefix_sum[i] - left < lower:
                    i += 1
                while j <= hi and prefix_sum[j] - left <= upper:
                    j += 1
                count += j - i
            prefix_sum[lo:hi+1] = sorted(prefix_sum[lo:hi+1])
            return count

        prefix_sum = [0] + list(itertools.accumulate(nums))
        return merge_sort(0, len(prefix_sum) - 1)
