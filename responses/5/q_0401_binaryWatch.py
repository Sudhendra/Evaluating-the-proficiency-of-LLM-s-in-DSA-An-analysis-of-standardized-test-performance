class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(n):
            count = 0
            while n:
                n &= (n - 1)
                count += 1
            return count
        
        def generate_times(num_leds, start, total_turned_on, time, res):
            if num_turned_on == total_turned_on:
                if hrs < 12 and mins < 60:
                    res.append(f"{hrs}:{mins:02}")
                return
            for i in range(start, len(time)):
                if i < 4:
                    hrs += time[i]
                    if hrs >= 12:
                        hrs -= time[i]
                        continue
                else:
                    mins += time[i]
                    if mins >= 60:
                        mins -= time[i]
                        continue
                generate_times(num_leds, i + 1, total_turned_on + 1, time, res)
                if i < 4:
                    hrs -= time[i]
                else:
                    mins -= time[i]
        
        time = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        res = []
        generate_times(10, 0, 0, time, res)
        return res