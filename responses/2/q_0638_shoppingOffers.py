class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(curr_needs):
            cost = sum(curr_needs[i] * price[i] for i in range(len(price))

            for sp in special:
                next_needs = [curr_needs[i] - sp[i] for i in range(len(price))]
                if all(x >= 0 for x in next_needs):
                    cost = min(cost, sp[-1] + dfs(next_needs))
            return cost

        return dfs(needs)
