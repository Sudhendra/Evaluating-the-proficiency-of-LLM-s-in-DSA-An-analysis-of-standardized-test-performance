class Solution:
    
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict

        def build_pyramid(row, next_row, row_idx):
            if len(row) == 1:  # Check if the pyramid has been successfully built
                return True
            
            if row_idx == len(row) - 1:  # Move to the next row
                return build_pyramid(next_row, "", 0)
            
            for perm in perms[(row[row_idx], row[row_idx + 1])]:  # Try all possible top blocks
                if build_pyramid(row, next_row + perm, row_idx + 1):
                    return True
                
            return False
        
        perms = defaultdict(list)
        for allow in allowed:
            perms[(allow[0], allow[1])].append(allow[2])
        
        return build_pyramid(bottom, "", 0)