class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        res = [0] * 10
        
        # frequency of each character in the input string
        res[0] = count['z']
        res[2] = count['w']
        res[4] = count['u']
        res[6] = count['x']
        res[8] = count['g']
        
        # frequency of each character after removing all used digits
        res[3] = count['h'] - res[8]
        res[5] = count['f'] - res[4]
        res[7] = count['s'] - res[6]
        res[9] = count['i'] - res[5] - res[6] - res[8]
        res[1] = count['n'] - 2 * res[9] - res[7]
        
        return ''.join(str(i) * res[i] for i in range(10))