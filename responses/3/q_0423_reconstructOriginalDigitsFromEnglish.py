class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 10
        for char in s:
            if char == "z": count[0] += 1
            if char == "w": count[2] += 1
            if char == "x": count[6] += 1
            if char == "s": count[7] += 1  # "seven" is the only word with 's'
            if char == "g": count[8] += 1
            if char == "u": count[4] += 1
            if char == "f": count[5] += 1  # "five" is the only word with 'f'
            if char == "h": count[3] += 1  # "three" is the only word with 'h'
            if char == "o": count[1] += 1  # "one", "zero", "two" and "four" have 'o'
            if char == "i": count[9] += 1  # "nine", "six" and "eight" have 'i'
        
        count[1] -= count[0] + count[2] + count[4]
        count[3] -= count[8]
        count[5] -= count[4]
        count[7] -= count[6]
        count[9] -= count[5] + count[6] + count[8]
        
        digits = ""
        for i in range(10):
            digits += str(i) * count[i]
        
        return digits