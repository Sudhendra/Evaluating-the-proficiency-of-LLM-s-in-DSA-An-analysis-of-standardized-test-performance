from typing import List

class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        n = len(quality)
        ans = float('inf')
        for captain in range(n):
            ratio = wage[captain] / quality[captain]
            prices = []
            for worker in range(n):
                price = ratio * quality[worker]
                if price < wage[worker]:
                    continue
                prices.append(price)
            if len(prices) < k:
                continue
            prices.sort()
            ans = min(ans, sum(prices[:k]))
        return ans
