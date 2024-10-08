from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        good_nums = set()

        for i in range(n):
            if fronts[i] == backs[i]:
                good_nums.discard(fronts[i])
            else:
                good_nums.add(fronts[i])
                good_nums.add(backs[i])

        min_good_num = float('inf')
        for num in good_nums:
            min_good_num = min(min_good_num, num)

        return min_good_num if min_good_num != float('inf') else 0
