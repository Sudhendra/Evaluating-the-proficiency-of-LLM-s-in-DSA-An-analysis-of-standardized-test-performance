from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        start = 0
        fruit_counts = Counter()
        
        for end in range(len(fruits)):
            fruit_counts[fruits[end]] += 1

            while len(fruit_counts) > 2:
                fruit_counts[fruits[start]] -= 1
                if fruit_counts[fruits[start]] == 0:
                    del fruit_counts[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits
