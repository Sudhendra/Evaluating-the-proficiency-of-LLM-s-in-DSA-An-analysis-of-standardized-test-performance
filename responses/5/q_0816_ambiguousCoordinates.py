from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def add_decimal(num):
            n = len(num)
            if n == 1 or num[0] != '0':
                result.append(num)
            for i in range(1, n):
                if (num[:i] == '0' or num[-1] == '0') and num[-1] != '0':
                    continue
                result.append(num[:i] + '.' + num[i:])

        s = s[1:-1]
        n = len(s)
        result = []
        for i in range(1, n):
            left, right = s[:i], s[i:]
            if (left[0] == '0' and len(left) > 1) or (right[-1] == '0' and right != '0'):
                continue
            left_options = []
            right_options = []
            add_decimal(left)
            add_decimal(right)
            for l in left_options:
                for r in right_options:
                    result.append('(' + l + ', ' + r + ')')
        return result
