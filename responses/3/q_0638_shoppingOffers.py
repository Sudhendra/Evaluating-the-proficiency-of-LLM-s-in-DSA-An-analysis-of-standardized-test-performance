class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping_helper(needs):
            nonlocal price, special

            # Calculate the total price without using any special offer
            total_price = sum([needs[i] * price[i] for i in range(len(needs)])

            # Check if any special offer can be applied
            for offer in special:
                for i in range(len(needs)):
                    if needs[i] < offer[i]:
                        break
                else:
                    # Apply the special offer
                    new_needs = [needs[i] - offer[i] for i in range(len(needs))]
                    total_price = min(total_price, offer[-1] + shopping_helper(new_needs))

            return total_price

        return shopping_helper(needs)