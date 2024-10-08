class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def expand(s):
            if '(' not in s:
                return float(s)
            integer_part, repeating_part = s.split('(')
            repeating_part = repeating_part[:-1]
            non_repeating_part = integer_part.split('.')[-1]
            repeating_length = len(repeating_part)
            non_repeating_length = len(non_repeating_part)
            
            numerator = int(integer_part.replace('.', '') + repeating_part) - int(non_repeating_part)
            denominator = 10 ** (non_repeating_length + repeating_length) - 10 ** non_repeating_length
            
            return numerator / denominator

        return abs(expand(s) - expand(t)) < 1e-9
