class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        basket = {}
        start = 0

        for end in range(len(fruits)):
            fruit = fruits[end]
            basket[fruit] = basket.get(fruit, 0) + 1

            while len(basket) > 2:
                fruit = fruits[start]
                basket[fruit] -= 1
                if basket[fruit] == 0:
                    del basket[fruit]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits