from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        num_freq = Counter(nums)
        pairs_count = 0

        for num in num_freq:
            if k == 0:
                if num_freq[num] > 1:
                    pairs_count += 1
            else:
                if num + k in num_freq:
                    pairs_count += 1

        return pairs_count
