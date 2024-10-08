from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        sorted_list = SortedList()
        for num in reversed(nums):
            count = sorted_list.bisect_left(num)
            counts.append(count)
            sorted_list.add(num)
        return counts
