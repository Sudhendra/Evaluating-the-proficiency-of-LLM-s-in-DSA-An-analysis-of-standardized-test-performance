from typing import List

class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        def shopping_helper(needs):
            nonlocal price, special

            # Base case: calculate price without using any special offer
            res = sum(needs[i] * price[i] for i in range(len(needs))

            # Check each special offer
            for sp in special:
                remaining_needs = [needs[i] - sp[i] for i in range(len(needs))]
                if min(remaining_needs) >= 0:  # Check if the current offer can be applied
                    res = min(res, sp[-1] + shopping_helper(remaining_needs))

            return res

        return shopping_helper(needs)

# Example usage
sol = Solution()
print(sol.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))  # Output: 14
print(sol.shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))  # Output: 11
