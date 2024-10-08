class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(input_str: str) -> str:
            result = []
            for char in input_str:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)
        
        return build_string(s) == build_string(t)
