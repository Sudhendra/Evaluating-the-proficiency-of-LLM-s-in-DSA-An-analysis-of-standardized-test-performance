from itertools import permutations, product

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def operate(a, b):
            return [a + b, a - b, b - a, a * b, a / b if b != 0 else float('inf'), b / a if a != 0 else float('inf')]

        def backtracking(nums):
            if len(nums) == 1:
                return nums[0] == 24

            for a, b, *rest in permutations(nums):
                for op in product(range(6), repeat=2):
                    if op[0] > 3 and a == 0:
                        continue
                    if op[1] > 3 and b == 0:
                        continue
                    next_nums = [operate(a, b)[o] for o in op] + rest
                    if backtracking(next_nums):
                        return True
            return False

        return backtracking(cards)
