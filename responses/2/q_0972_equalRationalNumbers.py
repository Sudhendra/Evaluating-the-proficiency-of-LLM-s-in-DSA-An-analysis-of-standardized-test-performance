class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(s):
            integer_part = non_repeating_part = repeating_part = 0

            if '(' in s:
                non_repeating_start = s.index('.') + 1
                non_repeating_end = s.index('(')
                repeating_end = len(s) - 1

                non_repeating_part = int(s[non_repeating_start:non_repeating_end])
                repeating_part = int(s[non_repeating_end + 1:repeating_end])
            else:
                if '.' in s:
                    non_repeating_part = int(s[s.index('.') + 1:])
                integer_part = int(s.split('.')[0])

            return integer_part, non_repeating_part, repeating_part

        s_int, s_non_rep, s_rep = parse(s)
        t_int, t_non_rep, t_rep = parse(t)

        # Compare the parsed components
        if s_rep or t_rep:
            if (s_int, s_non_rep, s_rep) != (t_int, t_non_rep, t_rep):
                return False
        else:
            if s_int != t_int or s_non_rep != t_non_rep:
                return False

        return True