class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        components = path.split("/")
        for comp in components:
            if comp == "..":
                if stack:
                    stack.pop()
            elif comp and comp != ".":
                stack.append(comp)

        return "/" + "/".join(stack)
