class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_components = path.split('/')

        for component in path_components:
            if component not in ['', '.', '..']:
                stack.append(component)
            elif component == '..' and stack:
                stack.pop()

        return '/' + '/'.join(stack)
