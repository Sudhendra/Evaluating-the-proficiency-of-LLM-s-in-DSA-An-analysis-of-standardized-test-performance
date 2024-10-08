from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0

        for x in pushed:
            stack.append(x)
            while stack and i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        return len(stack) == 0
