from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(arr, k):
            count = 0
            left = 0
            window_freq = Counter()
            for right in range(len(arr)):
                if window_freq[arr[right]] == 0:
                    k -= 1
                window_freq[arr[right]] += 1
                
                while k < 0:
                    window_freq[arr[left]] -= 1
                    if window_freq[arr[left]] == 0:
                        k += 1
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return at_most_k(nums, k) - at_most_k(nums, k-1)