class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0

        prev_value = 0
        for char in s:
            value = roman_dict[char]
            result += value
            if prev_value < value:
                result -= 2 * prev_value
            prev_value = value

        return result