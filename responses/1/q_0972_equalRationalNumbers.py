class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def normalize(num_str):
            if '(' in num_str:
                non_repeating, repeating = num_str.split('(')
                repeating = repeating[:-1]
                return non_repeating + repeating * 20, int(len(non_repeating) + len(repeating) * 20)
            return num_str, 20

        s_dec, s_digits = normalize(s)
        t_dec, t_digits = normalize(t)

        return float(s_dec) == float(t_dec)
