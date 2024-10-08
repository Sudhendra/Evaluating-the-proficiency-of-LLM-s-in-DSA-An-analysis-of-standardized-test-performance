class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        result = 0
        for k, v in count.items():
            result += (v // (k + 1)) * (k + 1)
            if v % (k + 1) != 0:
                result += k + 1
        return result
