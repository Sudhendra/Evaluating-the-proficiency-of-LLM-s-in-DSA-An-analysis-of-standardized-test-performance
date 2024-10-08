from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        digits = [0]*10

        digits[0] = count['z']
        digits[2] = count['w']
        digits[4] = count['u']
        digits[6] = count['x']
        digits[8] = count['g']

        digits[3] = count['h'] - digits[8]  # 'h' occurs in '3' and '8'
        digits[5] = count['f'] - digits[4]  # 'f' occurs in '4' and '5'
        digits[7] = count['s'] - digits[6]  # 's' occurs in '6' and '7'

        digits[1] = count['o'] - digits[0] - digits[2] - digits[4]
        digits[9] = count['i'] - digits[5] - digits[6] - digits[8']

        res = ''
        for i, digit in enumerate(digits):
            res += str(i)*digit

        return res
