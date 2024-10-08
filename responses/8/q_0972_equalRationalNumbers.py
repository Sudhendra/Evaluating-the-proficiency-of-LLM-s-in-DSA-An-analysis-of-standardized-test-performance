class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        import fractions
        
        def get_number(num_str):
            if '(' in num_str:
                integer_part, repeating_part = num_str.split('(')
                repeating_part = repeating_part[:-1]  # Remove closing bracket
                non_repeating_part, repeat_length = repeating_part.split('.')
                repeat_length = repeat_length[0]
                return int(integer_part or '0') * 10**len(non_repeating_part) + int(non_repeating_part), int(repeating_part), int(repeat_length)
            if '.' in num_str:
                integer_part, decimal_part = num_str.split('.')
                return int(integer_part or '0') * 10**len(decimal_part) + int(decimal_part), int(decimal_part), 0
            return int(num_str), 0, 0

        s_int, s_non_repeat, s_repeat = get_number(s)
        t_int, t_non_repeat, t_repeat = get_number(t)
        s_frac = fractions.Fraction(s_int * 10**s_repeat + s_non_repeat - s_int, 10**s_repeat - 1) if s_repeat else fractions.Fraction(s_int + s_non_repeat, 1)
        t_frac = fractions.Fraction(t_int * 10**t_repeat + t_non_repeat - t_int, 10**t_repeat - 1) if t_repeat else fractions.Fraction(t_int + t_non_repeat, 1)
        
        return s_frac == t_frac
