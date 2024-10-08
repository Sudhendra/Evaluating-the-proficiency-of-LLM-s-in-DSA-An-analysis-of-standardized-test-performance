from collections import deque

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort_count(left, right):
            if right - left <= 1:
                return 0
            
            mid = (left + right) // 2
            count = mergesort_count(left, mid) + mergesort_count(mid, right)
            j = mid
            for i in range(left, mid):
                while j < right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid
            
            nums[left:right] = sorted(nums[left:right])
            
            return count
        
        return mergesort_count(0, len(nums))
