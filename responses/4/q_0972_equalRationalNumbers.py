class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_decimal(num_str):
            if '(' in num_str:
                non_repeat, repeat = num_str.split('(')
                repeat = repeat[:-1]
                return float(non_repeat + repeat * 1000) / 9999
            return float(num_str)

        return abs(convert_to_decimal(s) - convert_to_decimal(t)) < 1e-9
