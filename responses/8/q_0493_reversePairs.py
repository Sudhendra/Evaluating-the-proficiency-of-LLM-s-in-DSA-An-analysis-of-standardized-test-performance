from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_and_count(lo, mid, hi):
            count = 0
            j = mid + 1
            for i in range(lo, mid + 1):
                while j <= hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            merged = []
            left, right = lo, mid + 1
            while left <= mid and right <= hi:
                if nums[left] <= nums[right]:
                    merged.append(nums[left])
                    left += 1
                else:
                    merged.append(nums[right])
                    right += 1
            
            while left <= mid:
                merged.append(nums[left])
                left += 1
            while right <= hi:
                merged.append(nums[right])
                right += 1
            
            nums[lo:hi+1] = merged
            return count
        
        def divide(lo, hi):
            if lo >= hi:
                return 0
            
            mid = lo + (hi - lo) // 2
            count = divide(lo, mid) + divide(mid + 1, hi)
            count += merge_and_count(lo, mid, hi)
            return count
        
        return divide(0, len(nums)-1)
