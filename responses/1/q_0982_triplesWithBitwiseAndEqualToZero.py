from collections import Counter

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = Counter([a & b & c for a in nums for b in nums for c in nums])
        return sum(count[x] for x in count)
