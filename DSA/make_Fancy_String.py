# LeetCode 1957: Delete Characters to Make Fancy String
# Aim: Modify the string so that no three consecutive characters are the same.
# Return the longest possible fancy string by deleting the minimum number of characters.


    def makeFancyString(self, s: str) -> str:
        result = []

        for char in s:
            if len(result) >= 2 and result[-1] == char and result[-2] == char:
                continue  
            result.append(char)

        return ''.join(result)
