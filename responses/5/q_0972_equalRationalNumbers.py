class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_decimal(s):
            if '(' not in s:
                if '.' in s:
                    int_part, dec_part = s.split('.')
                    return float(int_part + '.' + dec_part + '0' * 18)
                else:
                    return float(s + '.' + '0' * 18)
            else:
                int_part, dec_part = s.split('.')
                non_repeat, repeat = dec_part.split('(')
                repeat = repeat.rstrip(')')
                cycle_len = len(repeat)
                non_repeat = non_repeat + repeat * 18
                return float(int_part + '.' + non_repeat[:18] + '(' + repeat + ')')
        
        return abs(convert_to_decimal(s) - convert_to_decimal(t)) < 1e-16
