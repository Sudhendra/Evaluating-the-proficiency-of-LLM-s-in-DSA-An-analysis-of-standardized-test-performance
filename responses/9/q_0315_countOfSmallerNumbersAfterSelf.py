from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = []
        sorted_nums = SortedList()
        
        for num in reversed(nums):
            counts.append(sorted_nums.bisect_left(num))
            sorted_nums.add(num)
        
        return counts
