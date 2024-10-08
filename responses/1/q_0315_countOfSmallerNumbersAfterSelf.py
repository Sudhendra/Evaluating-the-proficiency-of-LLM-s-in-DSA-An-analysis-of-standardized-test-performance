from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = SortedList()
        counts = []

        for num in reversed(nums):
            counts.append(sorted_nums.bisect_left(num))
            sorted_nums.add(num)

        return list(reversed(counts))
