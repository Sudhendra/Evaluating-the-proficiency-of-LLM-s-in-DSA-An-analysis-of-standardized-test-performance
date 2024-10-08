from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(index, path, s, result):
            if index == len(s):
                result.append("".join(path))
                return
            
            if s[index].isalpha():
                backtrack(index + 1, path + [s[index].lower()], s, result)
                backtrack(index + 1, path + [s[index].upper()], s, result)
            else:
                backtrack(index + 1, path + [s[index]], s, result)
        
        result = []
        backtrack(0, [], s, result)
        return result