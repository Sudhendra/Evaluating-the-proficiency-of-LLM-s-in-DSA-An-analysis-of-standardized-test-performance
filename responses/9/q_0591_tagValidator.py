class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack:
                return False
                
            if code.startswith("<![CDATA[", i):
                i = code.find("]]>", i)
                if i == -1:
                    return False
                i += 3
            elif code.startswith("</", i):
                j = i + 2
                i = code.find(">", j)
                if i == -1:
                    return False
                tag_name = code[j:i]
                if not stack or stack.pop() != tag_name:
                    return False
                i += 1
            elif code.startswith("<", i):
                j = i + 1
                i = code.find(">", j)
                if i == -1:
                    return False
                tag_name = code[j:i]
                if not tag_name.isupper() or len(tag_name) < 1 or len(tag_name) > 9:
                    return False
                stack.append(tag_name)
                i += 1
            else:
                i += 1
        
        return not stack
