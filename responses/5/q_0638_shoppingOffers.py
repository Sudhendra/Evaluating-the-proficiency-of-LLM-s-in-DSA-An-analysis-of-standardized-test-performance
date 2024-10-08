from typing import List

class Solution:    
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def shopping(price, special, needs, memo):
            if tuple(needs) in memo:
                return memo[tuple(needs)]

            cost = sum([needs[i] * price[i] for i in range(len(needs)])

            for sp in special:
                new_needs = [needs[i] - sp[i] for i in range(len(needs))]
                if all(x >= 0 for x in new_needs):
                    cost = min(cost, sp[-1] + shopping(price, special, new_needs, memo))

            memo[tuple(needs)] = cost
            return cost

        return shopping(price, special, needs, {})

