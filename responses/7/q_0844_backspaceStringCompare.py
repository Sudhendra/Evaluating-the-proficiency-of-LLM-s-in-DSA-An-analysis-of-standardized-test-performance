class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return "".join(result)

        return build_string(s) == build_string(t)
