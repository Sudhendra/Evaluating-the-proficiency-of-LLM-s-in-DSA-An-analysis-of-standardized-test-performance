class Solution:
    
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        start = 0
        fruit_counts = {}
        
        for end in range(len(fruits)):
            fruit = fruits[end]
            fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1

            while len(fruit_counts) > 2:
                fruit_counts[fruits[start]] -= 1
                if fruit_counts[fruits[start]] == 0:
                    del fruit_counts[fruits[start]]
                start += 1
                
            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits