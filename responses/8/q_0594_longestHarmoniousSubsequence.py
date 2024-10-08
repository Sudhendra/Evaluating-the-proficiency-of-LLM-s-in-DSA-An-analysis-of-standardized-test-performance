from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        longest_harmonious = 0
        for num in count:
            if num + 1 in count:
                longest_harmonious = max(longest_harmonious, count[num] + count[num + 1])
        return longest_harmonious
