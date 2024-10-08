from itertools import permutations

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(num):
            return int(num**0.5)**2 == num
        
        def check_adjacency(a, b):
            return is_square(a + b)
        
        def backtracking(nums, path, visited):
            if len(path) == len(nums):
                self.count += 1
                return
            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i-1] and not visited[i-1]):
                    continue
                if path and not check_adjacency(path[-1], nums[i]):
                    continue
                visited[i] = True
                backtracking(nums, path + [nums[i]], visited)
                visited[i] = False
                
        self.count = 0
        nums.sort()
        backtracking(nums, [], [False]*len(nums))
        return self.count

# Example usage
solution = Solution()
print(solution.numSquarefulPerms([1, 17, 8]))  # Output: 2
print(solution.numSquarefulPerms([2, 2, 2]))  # Output: 1
