from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def get_decimal_parts(num: str) -> List[str]:
            n = len(num)
            if n == 1:
                return [num]

            if num[0] == "0" and num[n-1] == "0":
                return []

            if num[0] == "0":
                return ["0." + num[1:]]

            if num[n-1] == "0":
                return [num]

            parts = [num]
            for i in range(1, n):
                parts.append(num[:i] + "." + num[i:])
            return parts

        s = s[1:-1]
        n = len(s)
        result = []
        for i in range(1, n):
            left_parts = get_decimal_parts(s[:i])
            right_parts = get_decimal_parts(s[i:])
            for left in left_parts:
                for right in right_parts:
                    result.append("(" + left + ", " + right + ")")
        return result
