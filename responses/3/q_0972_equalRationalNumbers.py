class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_decimal(s):
            if '.' not in s:
                return int(s), 0

            integer_part, decimal_part = s.split('.')
            if '(' not in decimal_part:
                return int(integer_part), float(s)
            non_repeating_part, repeating_part = decimal_part.split('(')
            repeating_part = repeating_part[:-1]  # Remove the ')'

            non_repeating_value = float('0.' + non_repeating_part if non_repeating_part else '0')
            repeating_value = float('0.' + repeating_part)

            return int(integer_part), non_repeating_value + repeating_value / (10**len(non_repeating_part + repeating_part) - 1)

        float_s = convert_to_decimal(s)
        float_t = convert_to_decimal(t)

        return float_s == float_t