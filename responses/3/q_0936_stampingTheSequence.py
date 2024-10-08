class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check_valid(index):
            stamped = False
            for i in range(len(stamp)):
                if target[index+i] == '?':
                    continue
                if target[index+i] != stamp[i]:
                    return False
                stamped = True
            return stamped
        
        n, m = len(target), len(stamp)
        target = list(target)
        result = []
        done = 0
        while done < n:
            stamped = False
            for i in range(n - m + 1):
                if check_valid(i):
                    done += self.replace_stamped(target, i, m)
                    result.append(i)
                    stamped = True
            if not stamped:
                return []
        return result[::-1]
    
    def replace_stamped(self, target, start, m):
        count = 0
        for i in range(m):
            if target[start + i] != '?':
                target[start + i] = '?'
                count += 1
        return count
