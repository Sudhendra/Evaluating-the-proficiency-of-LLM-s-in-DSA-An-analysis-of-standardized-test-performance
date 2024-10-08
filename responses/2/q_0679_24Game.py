from itertools import permutations, product

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        ops = ['+', '-', '*', '/']

        def evaluate(a, b, op):
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/' and b != 0:
                return a / b
            return None

        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for perm in permutations(nums):
                for i in range(1, len(perm)):
                    for op in ops:
                        if (op == '+' or op == '*') and i > 1:
                            continue
                        if op == '/' and perm[i] == 0:
                            continue
                        new_nums = [evaluate(perm[j], perm[j+1], op) if j == i-1 else perm[j] for j in range(len(perm)-1)]
                        if backtrack(new_nums):
                            return True
            return False

        return backtrack(cards)
