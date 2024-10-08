from typing import List

class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def can_apply_offer(needs, offer):
            for i in range(len(needs)):
                if needs[i] < offer[i]:
                    return False
            return True

        def apply_offer(needs, offer):
            for i in range(len(needs)):
                needs[i] -= offer[i]
            return needs

        def min_cost(price, special, needs, memory):
            needs_tuple = tuple(needs)
            if needs_tuple in memory:
                return memory[needs_tuple]

            cost = sum(p * n for p, n in zip(price, needs))

            for offer in special:
                if can_apply_offer(needs, offer):
                    new_needs = apply_offer(needs[:], offer)
                    cost = min(cost, offer[-1] + min_cost(price, special, new_needs, memory))

            memory[needs_tuple] = cost
            return cost

        return min_cost(price, special, needs, {})

# Additional test cases
solution = Solution()
print(solution.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))  # Output: 14
print(solution.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))  # Output: 11
