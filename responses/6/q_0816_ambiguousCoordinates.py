from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def add_decimal(num):
            result = []
            for i in range(1, len(num)):
                left, right = num[:i], num[i:]
                if (not left.startswith('0') or left == '0') and (not right.endswith('0')):
                    result.append(left + '.' + right)
            if not num.startswith('0') or num == '0':
                result.append(num)
            return result

        def generate_nums(num):
            result = []
            for i in range(1, len(num)):
                left, right = num[:i], num[i:]
                left_nums = add_decimal(left)
                right_nums = add_decimal(right)
                for l in left_nums:
                    for r in right_nums:
                        result.append('(' + l + ', ' + r + ')')
            return result

        s = s[1:-1]
        output = []
        for i in range(1, len(s)):
            left_nums = generate_nums(s[:i])
            right_nums = generate_nums(s[i:])
            for l in left_nums:
                for r in right_nums:
                    output.append(l + r)

        return output
