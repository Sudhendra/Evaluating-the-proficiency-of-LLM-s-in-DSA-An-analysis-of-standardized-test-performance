front_matter = {
    "qid": 518,
    "title": "Coin Change II",
    "titleSlug": "coin-change-ii",
    "difficulty": "Medium",
    "tags": ["Array", "Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]