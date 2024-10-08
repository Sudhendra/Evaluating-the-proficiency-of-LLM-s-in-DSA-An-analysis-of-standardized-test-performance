from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(remain):
            nonlocal price, special, memo
            if tuple(remain) in memo:
                return memo[tuple(remain)]

            # Calculate total price without any special offer
            result = sum(p * r for p, r in zip(price, remain))

            # Try each special offer
            for spec in special:
                new_remain = [r - s for r, s in zip(remain, spec[:-1])]
                if all(r >= 0 for r in new_remain):
                    result = min(result, spec[-1] + dfs(new_remain))

            memo[tuple(remain)] = result
            return result

        memo = {}
        return dfs(needs)
