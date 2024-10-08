class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack:
                return False
            if code.startswith("<![CDATA[", i):
                j = i + 9
                i = code.find("]]>", j)
                if i == -1:
                    return False
                i += 2
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
                if i == -1:
                    return False
                tag = code[j:i]
                if not tag.isupper() or len(tag) > 9:
                    return False
                stack.append(tag)
            else:
                i += 1

        return not stack

# Additional solutions can be added as new methods of the Solution class if needed.