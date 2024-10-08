from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = SortedList()
        counts = []

        for num in reversed(nums):
            count = sorted_nums.bisect_left(num)
            counts.append(count)
            sorted_nums.add(num)

        return counts
