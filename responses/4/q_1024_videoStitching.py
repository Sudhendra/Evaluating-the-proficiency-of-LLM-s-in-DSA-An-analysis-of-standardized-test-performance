from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [float('inf')] * (time + 1)
        dp[0] = 0

        for i in range(1, time + 1):
            for clip in clips:
                start, end = clip
                if start <= i <= end:
                    dp[i] = min(dp[i], dp[start] + 1)

        return dp[time] if dp[time] != float('inf') else -1
