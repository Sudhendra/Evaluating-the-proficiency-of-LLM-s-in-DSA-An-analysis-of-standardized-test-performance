from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def is_valid_number(num_str):
            if len(num_str) == 1:
                return True
            if num_str[0] != '0':
                return True
            if num_str[1] == '0':
                return False
            return True

        def get_decimal_parts(int_part):
            result = []
            for i in range(1, len(int_part)):
                decimal_part = int_part[:i] + '.' + int_part[i:]
                if is_valid_number(int_part) and is_valid_number(decimal_part):
                    result.append(decimal_part)
            return result

        def generate_coordinates(s):
            s = s[1:-1]
            n = len(s)
            result = []
            for i in range(1, n):
                int_part = s[:i]
                decimal_part = s[i:]
                for int_num in get_decimal_parts(int_part):
                    for dec_num in get_decimal_parts(decimal_part):
                        result.append(f"({int_num}, {dec_num})")
            return result

        return generate_coordinates(s)
