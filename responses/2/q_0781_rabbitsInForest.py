class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        res = 0
        
        for key, value in count.items():
            if key == 0:
                res += value
            else:
                res += (value // (key + 1)) * (key + 1)
                if value % (key + 1) != 0:
                    res += key + 1
        
        return res