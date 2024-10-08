from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        left = 0
        fruit_count = Counter()
        
        for right, fruit in enumerate(fruits):
            fruit_count[fruit] += 1
            
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1
                
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits
