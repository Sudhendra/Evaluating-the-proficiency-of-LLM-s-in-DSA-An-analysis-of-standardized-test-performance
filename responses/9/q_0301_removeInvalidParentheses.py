from typing import List

class Solution:
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            cnt = 0
            for char in s:
                if char == '(':
                    cnt += 1
                elif char == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        
        def backtrack(start, left_count, right_count, left_rem, right_rem, path, result)
            if start == len(s):
                if left_rem == 0 and right_rem == 0:
                    if is_valid(path):
                        result.add(path)
                return
            if s[start] == '(' and left_rem > 0:
                backtrack(start+1, left_count, right_count, left_rem-1, right_rem, path, result)
            if s[start] == ')' and right_rem > 0:
                backtrack(start+1, left_count, right_count, left_rem, right_rem-1, path, result)
            path += s[start]
            if s[start] != '(' and s[start] != ')':
                backtrack(start+1, left_count, right_count, left_rem, right_rem, path, result)
            elif s[start] == '(':
                backtrack(start+1, left_count+1, right_count, left_rem, right_rem, path, result)
            elif s[start] == ')' and left_count > right_count:
                backtrack(start+1, left_count, right_count+1, left_rem, right_rem, path, result)
            path = path[:-1]
        
        left_rem, right_rem = 0, 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
        
        result = set()
        path = ""
        backtrack(0, 0, 0, left_rem, right_rem, path, result)
        
        return list(result)
