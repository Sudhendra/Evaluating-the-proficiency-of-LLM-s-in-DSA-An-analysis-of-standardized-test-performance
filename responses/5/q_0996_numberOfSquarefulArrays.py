from itertools import permutations

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            root = int(num ** 0.5)
            return root * root == num
        
        def is_squareful(a, b):
            return is_square(a + b)
        
        def backtrack(curr_perm, visited):
            if len(curr_perm) == len(nums):
                self.count += 1
                return

            for i, num in enumerate(nums):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue

                if not curr_perm or is_squareful(curr_perm[-1], num):
                    visited[i] = True
                    curr_perm.append(num)
                    backtrack(curr_perm, visited)
                    curr_perm.pop()
                    visited[i] = False
        
        self.count = 0
        nums.sort()
        backtrack([], [False]*len(nums))
        return self.count
