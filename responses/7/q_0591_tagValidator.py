class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack:
                return False
            if code.startswith("<![CDATA[", i):
                j = i + 9
                i = code.index("]]>", j)
                if i == -1:
                    return False
                i += 2
            elif code.startswith("</", i):
                j = i + 2
                i = code.index(">", j)
                if i == -1:
                    return False
                tag = code[j:i]
                if not stack or stack.pop() != tag:
                    return False
                i += 1
            elif code.startswith("<", i):
                j = i + 1
                i = code.index(">", j)
                if i == -1:
                    return False
                tag = code[j:i]
                if not tag.isupper() or len(tag) > 9:
                    return False
                stack.append(tag)
                i += 1
            else:
                i += 1
        return not stack
