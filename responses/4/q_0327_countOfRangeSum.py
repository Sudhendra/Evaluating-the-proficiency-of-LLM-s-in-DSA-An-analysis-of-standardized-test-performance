from sortedcontainers import SortedList

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def countRangeSumRecursive(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            
            count = countRangeSumRecursive(lo, mid) + countRangeSumRecursive(mid, hi)
            
            j, k = mid, mid
            for i in range(lo, mid):
                while j < hi and prefix_sum[j] - prefix_sum[i] < lower:
                    j += 1
                while k < hi and prefix_sum[k] - prefix_sum[i] <= upper:
                    k += 1
                count += k - j
            
            sorted_prefix_sum[lo:hi] = sorted(prefix_sum[lo:hi])
            return count
        
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        sorted_prefix_sum = SortedList()
        return countRangeSumRecursive(0, len(prefix_sum))

