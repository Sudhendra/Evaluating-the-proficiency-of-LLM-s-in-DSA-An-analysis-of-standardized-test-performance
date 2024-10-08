class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(input_string):
            result = []
            for char in input_string:
                if char == '#':
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return ''.join(result)
        
        return build_string(s) == build_string(t)