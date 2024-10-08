from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def generate_combinations(num_str):
            n = len(num_str)
            if n == 1:  # If the input is a single digit, return it as is
                return [num_str]
            if num_str[0] == "0" and num_str[-1] == "0":  # Ignore leading and trailing zeros
                if num_str == "0":
                    return [num_str]
                else:
                    return []
            if num_str[0] == "0":  # If there's a leading zero, it can't have a decimal point
                return [num_str[:1] + "." + num_str[1:]]
            if num_str[-1] == "0":  # If there's a trailing zero, it can't have a decimal point
                return [num_str] if num_str[0] != "0" else []
            # Generate combinations by placing a decimal point at different positions
            res = [num_str]
            for i in range(1, n):
                res.append(num_str[:i] + "." + num_str[i:])
            return res

        s = s[1:-1]  # Remove the '(' at the beginning and ')' at the end of the input string
        result = []
        for i in range(1, len(s)):
            left_nums = generate_combinations(s[:i])
            right_nums = generate_combinations(s[i:])
            for left_num in left_nums:
                for right_num in right_nums:
                    result.append(f"({left_num}, {right_num})")
        return result
