class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                left_stack.append(i)
            elif s[i] == '*':
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while left_stack and star_stack:
            if left_stack[-1] < star_stack[-1]:
                left_stack.pop()
                star_stack.pop()
            else:
                break
        
        return len(left_stack) == 0
