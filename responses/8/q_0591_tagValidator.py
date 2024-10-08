class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        
        while i < len(code):
            if i > 0 and not stack:
                return False
            
            if code.startswith("<![CDATA[", i):
                i += 9
                while i < len(code) and not code.startswith("]]>", i):
                    i += 1
                i += 2
            elif code.startswith("</", i):
                j = i + 2
                i = code.find(">", j)
                if i < 0:
                    return False
                tag = code[j: i]
                if not stack or stack.pop() != tag:
                    return False
            elif code.startswith("<", i):
                j = i + 1
                i = code.find(">", j)
                if i < 0 or i - j < 1 or i - j > 9:
                    return False
                tag = code[j: i]
                for c in tag:
                    if not c.isupper():
                        return False
                stack.append(tag)
            else:
                i += 1
        
        return not stack
