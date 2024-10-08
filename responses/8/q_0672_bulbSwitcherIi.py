class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return min(2, presses + 1)
        if n == 2:
            return min(3, 1 << min(2, presses))
        if n >= 3:
            if presses == 0:
                return 1
            if presses == 1:
                return min(4, 1 << min(3, n))
            if presses == 2:
                return min(7, 1 << min(4, n))
            return min(8, 1 << min(4, n))

# Additional solution method
# class Solution:
#     def flipLights(self, n: int, presses: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return min(2, presses + 1)
#         if n == 2:
#             return min(3, 1 << min(2, presses))
#         if n >= 3:
#             if presses == 0:
#                 return 1
#             if presses == 1:
#                 return min(4, 1 << min(3, n))
#             if presses == 2:
#                 return min(7, 1 << min(4, n))
#             return min(8, 1 << min(4, n))
