from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_freq = defaultdict(int)
        sum_freq[0] = 1
        
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += sum_freq[prefix_sum]
            sum_freq[prefix_sum] += 1
        
        return count
