class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        skip = {"", ".", ".."}
        
        for dir in path.split("/"):
            if dir == ".." and stack:
                stack.pop()
            elif dir not in skip:
                stack.append(dir)
        
        return "/" + "/".join(stack)
