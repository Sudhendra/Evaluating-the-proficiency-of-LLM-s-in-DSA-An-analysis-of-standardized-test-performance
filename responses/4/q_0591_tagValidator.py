class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        
        while i < len(code):
            if i > 0 and not stack:
                return False
            
            if code.startswith("<![CDATA[", i):
                i += len("<![CDATA[")
                if not stack:
                    return False
                
                while i < len(code):
                    if code.startswith("]]>", i):
                        break
                    i += 1
                
            elif code.startswith("</", i):
                j = i + 2
                i = code.find(">", j)
                if i == -1:
                    return False
                
                tag = code[j:i]
                if not stack or stack.pop() != tag:
                    return False
                
            elif code.startswith("<", i):
                j = i + 1
                i = code.find(">", j)
                if i == -1 or not all(c.isupper() for c in code[j:i]) or i - j < 1 or i - j > 9:
                    return False
                
                tag = code[j:i]
                stack.append(tag)
                
            i += 1
        
        return not stack
