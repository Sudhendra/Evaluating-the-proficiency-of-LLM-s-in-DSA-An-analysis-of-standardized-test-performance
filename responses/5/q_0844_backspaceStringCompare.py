class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(s: str) -> str:
            result = []
            for char in s:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)
        
        return build_string(s) == build_string(t)
