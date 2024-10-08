from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        sorted_list = SortedList()
        for num in reversed(nums):
            pos = sorted_list.bisect_left(num)
            ans.append(pos)
            sorted_list.add(num)
        return ans
