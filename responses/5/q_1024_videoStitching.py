from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        dp = [float('inf')] * (time + 1)
        dp[0] = 0

        for start, end in clips:
            for t in range(end, start - 1, -1):
                if dp[t] > dp[end] + 1:
                    dp[t] = dp[end] + 1

        return dp[time] if dp[time] != float('inf') else -1
