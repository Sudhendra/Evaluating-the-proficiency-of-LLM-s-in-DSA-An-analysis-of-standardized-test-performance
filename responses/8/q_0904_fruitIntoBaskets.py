from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        start = 0
        basket = Counter()
        
        for end in range(len(fruits)):
            basket[fruits[end]] += 1
            
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1
            
            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits
