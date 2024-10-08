class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse_num(num_str: str) -> float:
            if '(' in num_str:
                non_repeating, repeating = num_str.split('(')
                repeating = repeating[:-1]
                return float(non_repeating + repeating * 10**9) / (10**len(non_repeating) * (10**len(repeating) - 1))
            return float(num_str)

        return abs(parse_num(s) - parse_num(t)) < 1e-9
