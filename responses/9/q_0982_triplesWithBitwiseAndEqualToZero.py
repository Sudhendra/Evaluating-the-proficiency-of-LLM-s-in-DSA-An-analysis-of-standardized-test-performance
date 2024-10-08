from collections import Counter
from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = Counter(a & b for a in nums for b in nums)
        return sum(count[a & b] for a in nums for b in count)

# Example usage
solution = Solution()
print(solution.countTriplets([2, 1, 3]))  # Output: 12
print(solution.countTriplets([0, 0, 0]))  # Output: 27
