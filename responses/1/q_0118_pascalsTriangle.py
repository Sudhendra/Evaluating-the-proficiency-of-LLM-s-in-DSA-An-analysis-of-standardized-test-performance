class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        result = [[1]]
        
        for i in range(1, numRows):
            prev_row = result[-1]
            new_row = [1]
            
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j - 1] + prev_row[j])
            
            new_row.append(1)
            result.append(new_row)
        
        return result