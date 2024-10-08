front_matter = {
    "qid": 714,
    "title": "Best Time to Buy and Sell Stock with Transaction Fee",
    "titleSlug": "best-time-to-buy-and-sell-stock-with-transaction-fee",
    "difficulty": "Medium",
    "tags": ["Array", "Dynamic Programming", "Greedy"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
from typing import List

class Solution:
    """
    You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^{th}` day, and an integer `fee` representing a transaction fee.

    Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

    **Note:**

    * You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
    * The transaction fee is only charged once for each stock purchase and sale.
    """

    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        
        return cash
# If you have multiple solutions, add them all here as methods of the same class.