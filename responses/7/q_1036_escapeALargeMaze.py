class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        def is_bounded(x, y):
            return 0 <= x < 10**6 and 0 <= y < 10**6

        def is_escape_possible(source, target):
            blocked_set = set(tuple(b) for b in blocked)

            visited = set()
            stack = [tuple(source)]

            while stack:
                x, y = stack.pop()
                if (x, y) == tuple(target):
                    return True

                if not is_bounded(x, y) or (x, y) in visited or (x, y) in blocked_set:
                    continue

                visited.add((x, y))

                stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

                if len(visited) >= 20000:
                    return True

            return False

        return is_escape_possible(source, target) and is_escape_possible(target, source)
