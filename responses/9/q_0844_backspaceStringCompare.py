class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def final_string(input_string):
            result = []
            for char in input_string:
                if char == "#":
                    if result:
                        result.pop()
                else:
                    result.append(char)
            return "".join(result)
        
        return final_string(s) == final_string(t)
