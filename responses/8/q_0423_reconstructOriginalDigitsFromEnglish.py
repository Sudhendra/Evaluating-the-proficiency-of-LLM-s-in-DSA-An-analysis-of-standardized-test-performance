from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        digits = []

        def remove_digit(char_count, digit, word):
            for c in word:
                char_count[c] -= char_count[c]

            for i in range(char_count[digit]):
                digits.append(str(digit))
                for c in word:
                    char_count[c] -= 1

        remove_digit(count, 0, "zero")
        remove_digit(count, 2, "two")
        remove_digit(count, 4, "four")
        remove_digit(count, 6, "six")
        remove_digit(count, 8, "eight")
        remove_digit(count, 1, "one")
        remove_digit(count, 3, "three")
        remove_digit(count, 5, "five")
        remove_digit(count, 7, "seven")
        remove_digit(count, 9, "nine")

        return ''.join(sorted(digits))
