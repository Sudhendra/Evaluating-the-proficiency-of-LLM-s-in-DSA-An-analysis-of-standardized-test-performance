from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [0] + [float('inf')] * time

        for i in range(1, time + 1):
            for start, end in clips:
                if start < i <= end:
                    dp[i] = min(dp[i], dp[start] + 1)

        return -1 if dp[time] == float('inf') else dp[time]
