class Solution:
    def originalDigits(self, s: str) -> str:
        word_count = {}
        for char in s:
            word_count[char] = word_count.get(char, 0) + 1

        digit_count = [0] * 10
        digit_count[0] = word_count.get("z", 0)
        digit_count[2] = word_count.get("w", 0)
        digit_count[4] = word_count.get("u", 0)
        digit_count[6] = word_count.get("x", 0)
        digit_count[8] = word_count.get("g", 0)
        digit_count[3] = word_count.get("h", 0) - digit_count[8]
        digit_count[5] = word_count.get("f", 0) - digit_count[4]
        digit_count[7] = word_count.get("s", 0) - digit_count[6]
        digit_count[9] = word_count.get("i", 0) - digit_count[5] - digit_count[6] - digit_count[8]
        digit_count[1] = word_count.get("n", 0) - 2 * digit_count[9] - digit_count[7]

        result = ""
        for i in range(10):
            result += str(i) * digit_count[i]
        
        return result
