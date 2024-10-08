from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def add_decimal(s):
            if not s or (len(s) > 1 and s[0] == '0' and s[-1] == '0'):
                return []
            if s[-1] == '0':
                return [s]
            if s[0] == '0':
                return [s[0] + '.' + s[1:]]
            return [s] + [s[:i] + '.' + s[i:] for i in range(1, len(s))]

        s = s[1:-1]

        result = []
        for i in range(1, len(s)):
            left = add_decimal(s[:i])
            right = add_decimal(s[i:])
            for l in left:
                for r in right:
                    result.append(f'({l}, {r})')

        return result

# Example usage
solution = Solution()
output = solution.ambiguousCoordinates("(123)")
print(output)
