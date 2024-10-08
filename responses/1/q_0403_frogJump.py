class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False

        dp = {}
        
        for stone in stones:
            dp[stone] = set()
        
        dp[0].add(1)

        for stone in stones:
            for step in dp[stone]:
                for next_step in range(max(step - 1, 1), step + 2):
                    next_stone = stone + next_step
                    if next_stone == stones[-1]:
                        return True
                    if next_stone in dp:
                        dp[next_stone].add(next_step)

        return False