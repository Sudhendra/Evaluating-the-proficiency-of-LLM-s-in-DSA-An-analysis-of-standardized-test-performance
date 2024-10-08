class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def to_float(s: str) -> float:
            if '(' in s:
                non_repeating_part, repeating_part = s.split('(')
                repeating_part = repeating_part[:-1]  # Remove closing bracket
                return float(non_repeating_part + repeating_part * 10) / (10**(len(non_repeating_part) + len(repeating_part))

            return float(s)

        return abs(to_float(s) - to_float(t)) < 1e-9
