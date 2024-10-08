class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        digits = {
            '0': count['z'],
            '2': count['w'],
            '4': count['u'],
            '6': count['x'],
            '8': count['g'],
            '3': count['h'] - count['8'],
            '5': count['f'] - count['4'],
            '7': count['s'] - count['6'],
            '9': count['i'] - count['5'] - count['6'] - count['8'],
            '1': count['o'] - count['0'] - count['2'] - count['4']
        }
        result = ''
        for digit, num in digits.items():
            result += digit * num
        return result