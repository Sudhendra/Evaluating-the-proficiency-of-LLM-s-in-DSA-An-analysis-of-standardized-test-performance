from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def merge_sort(lo, hi):
            mid = lo + (hi - lo) // 2
            if mid == lo:
                return 0
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            i = j = mid
            for left in range(lo, mid):
                while i < hi and prefix[i] - prefix[left] < lower:
                    i += 1
                while j < hi and prefix[j] - prefix[left] <= upper:
                    j += 1
                count += j - i
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        return merge_sort(0, len(prefix))

# Additional solutions can be added as extra methods within the Solution class
