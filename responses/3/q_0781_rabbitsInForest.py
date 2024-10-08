class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        total = 0
        for num, cnt in count.items():
            total += (cnt // (num + 1)) * (num + 1)
            if cnt % (num + 1) != 0:
                total += num + 1
        return total