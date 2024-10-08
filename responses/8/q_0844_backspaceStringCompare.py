class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(input_str):
            result = []
            for char in input_str:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return "".join(result)
        
        return process_string(s) == process_string(t)
