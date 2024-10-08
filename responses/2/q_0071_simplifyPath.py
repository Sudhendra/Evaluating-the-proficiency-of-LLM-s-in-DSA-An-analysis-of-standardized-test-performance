class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for dir in path.split("/"):
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir and dir != ".":
                stack.append(dir)

        return "/" + "/".join(stack)