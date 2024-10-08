from typing import List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def shopping(needs):
            nonlocal price, special
            cost = sum([needs[i] * price[i] for i in range(len(needs))])
            
            for spec in special:
                remaining_needs = []
                for i in range(len(needs)):
                    remaining = needs[i] - spec[i]
                    if remaining < 0:
                        remaining_needs = []
                        break
                    remaining_needs.append(remaining)
                    
                if remaining_needs:
                    cost = min(cost, spec[-1] + shopping(remaining_needs))
                    
            return cost
        
        return shopping(needs)
