from typing import List

class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def shopping_helper(needs):
            cost = sum(needs[i] * price[i] for i in range(len(needs)))

            for offer in special:
                temp_needs = [needs[i] - offer[i] for i in range(len(needs))]
                if min(temp_needs) >= 0:
                    cost = min(cost, offer[-1] + shopping_helper(temp_needs))

            return cost

        return shopping_helper(needs)
