class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(text: str) -> str:
            result = []
            for char in text:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return ''.join(result)
        
        return build_string(s) == build_string(t)