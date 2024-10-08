from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        num_counts = Counter(nums)
        unique_pairs = set()

        for num in num_counts:
            if k == 0:
                if num_counts[num] > 1:
                    unique_pairs.add((num, num))
            else:
                if num + k in num_counts:
                    unique_pairs.add((num, num + k))

        return len(unique_pairs)
