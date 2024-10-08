from typing import List

class Solution:

    def ambiguousCoordinates(self, s: str) -> List[str]:
        def get_valid_numbers(num_str):
            if len(num_str) == 1 or num_str[0] != '0':
                yield num_str
            for i in range(1, len(num_str)):
                if (num_str.startswith('0') and i == 1) or num_str.endswith('0'):
                    continue
                yield num_str[:i] + '.' + num_str[i:]

        s = s[1:-1]
        n = len(s)
        result = []

        for i in range(1, n):
            for x in get_valid_numbers(s[:i]):
                for y in get_valid_numbers(s[i:]):
                    result.append(f'({x}, {y})')

        return result
