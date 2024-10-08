class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        res = []

        # Order: "zero", "two", "four", "six", "eight", "three", "seven", "five", "nine", "one"

        digits = [
            (0, 'z', "zero"),
            (2, 'w', "two"),
            (4, 'u', "four"),
            (6, 'x', "six"),
            (8, 'g', "eight"),
            (3, 'h', "three"),
            (7, 's', "seven"),
            (5, 'v', "five"),
            (9, 'i', "nine"),
            (1, 'o', "one")
        ]

        for digit, unique_char, word in digits:
            count_digit = count.get(unique_char, 0)
            if count_digit > 0:
                res.extend([str(digit)] * count_digit)
                for c in word:
                    count[c] -= count_digit

        return ''.join(sorted(res))
