from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def get_valid_numbers(num: str) -> List[str]:
            n = len(num)
            if n == 1 or num[0] != '0':
                yield num
            for i in range(1, n):
                if (num[:i] == '0' or num[0] != '0') and num[-1] != '0':
                    yield f"{num[:i]}.{num[i:]}"
        
        def get_coordinates(num: str) -> List[str]:
            n = len(num)
            for i in range(1, n):
                for x in get_valid_numbers(num[:i]):
                    for y in get_valid_numbers(num[i:]):
                        yield f"({x}, {y})"
        
        s = s[1:-1]
        n = len(s)
        result = []
        for i in range(1, n):
            for x in get_coordinates(s[:i]):
                for y in get_coordinates(s[i:]):
                    result.append(f"{x}, {y}")
        
        return result
