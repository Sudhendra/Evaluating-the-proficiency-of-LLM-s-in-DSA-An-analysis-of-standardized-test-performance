class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_length = {0: 0}
        
        for line in input.split('\n'):
            depth = line.count('\t')
            name = line.replace('\t', '')
            
            if '.' in name:
                max_len = max(max_len, path_length[depth] + len(name))
            else:
                path_length[depth + 1] = path_length[depth] + len(name) + 1
                
        return max_len
