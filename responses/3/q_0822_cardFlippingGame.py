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

        min_good = min(num for num in good_nums) if good_nums else 0
        return min_good