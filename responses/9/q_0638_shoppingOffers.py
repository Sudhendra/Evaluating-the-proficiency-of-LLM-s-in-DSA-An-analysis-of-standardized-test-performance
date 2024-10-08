from typing import List

class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def dfs(needs):
            nonlocal price, special

            # Check if using specials is more expensive than individual items
            cost = sum(needs[i] * price[i] for i in range(len(needs)))
            
            for offer in special:
                new_needs = [needs[i] - offer[i] for i in range(len(needs))]
                if min(new_needs) >= 0:
                    cost = min(cost, offer[-1] + dfs(new_needs))

            return cost

        return dfs(needs)
