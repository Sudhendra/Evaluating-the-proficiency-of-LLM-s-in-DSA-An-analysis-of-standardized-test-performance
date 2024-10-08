from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        digit_count = {}
        digit_count['0'] = count['z']
        digit_count['2'] = count['w']
        digit_count['4'] = count['u']
        digit_count['6'] = count['x']
        digit_count['8'] = count['g']
        digit_count['3'] = count['h'] - digit_count['8']
        digit_count['5'] = count['f'] - digit_count['4']
        digit_count['7'] = count['s'] - digit_count['6']
        digit_count['9'] = count['i'] - digit_count['5'] - digit_count['6'] - digit_count['8']
        digit_count['1'] = count['n'] - digit_count['7'] - 2 * digit_count['9']

        result = ''
        for digit, times in digit_count.items():
            result += digit * times
        return result
