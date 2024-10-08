from sortedcontainers import SortedList

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        def count_while_merge_sort(lo, hi):
            if lo == hi:
                return 0
            mid = (lo + hi) // 2
            count = count_while_merge_sort(lo, mid) + count_while_merge_sort(mid+1, hi)
            
            temp = []
            j, k = mid+1, mid+1
            for i in range(lo, mid+1):
                while j <= hi and prefix_sum[j] - prefix_sum[i] < lower:
                    j += 1
                while k <= hi and prefix_sum[k] - prefix_sum[i] <= upper:
                    k += 1
                while p <= hi and prefix_sum[p] < prefix_sum[i]:
                    temp.append(prefix_sum[p])
                    p += 1
                temp.append(prefix_sum[i])
                count += k - j
            prefix_sum[lo:lo+len(temp)] = temp
            return count

        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return count_while_merge_sort(0, len(prefix_sum)-1)
