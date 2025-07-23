# Problem: Binary Watch
# Aim: Generate all possible valid times on a binary watch where a given number of LEDs are turned on.
# The watch has 4 LEDs for hours (0–11) and 6 LEDs for minutes (0–59).
# Approach: Iterate through all hour and minute combinations and select those 
# where the total count of '1's in their binary representation equals the given number.

class Solution:
    def readBinaryWatch(self, turnedOn):
        result = []

        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == turnedOn:
                    result.append(f"{h}:{m:02d}")

        return result
