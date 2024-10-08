from collections import defaultdict

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        dp = defaultdict(set)
        dp[1] = set([1])

        for stone in stones[1:]:
            for step in dp[stone]:
                for next_step in range(step-1, step+2):
                    if next_step > 0 and stone + next_step in stones:
                        if stone + next_step == stones[-1]:
                            return True
                        dp[stone + next_step].add(next_step)

        return False
