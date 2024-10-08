from collections import Counter

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        moves = 0
        taken = set()

        for num, freq in counter.items():
            while freq > 1:
                num += 1
                moves += num - counter[num] if num not in taken else 0
                taken.add(num)
                freq -= 1

        return moves
