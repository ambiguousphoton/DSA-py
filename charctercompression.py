class Solution:
    def Compress(string):
        previous_char = ''
        current_streak = 0
        compressed_string = ''
        for i, char in enumerate(string):
            if previous_char != char:
                if current_streak > 0:compressed_string += str(current_streak)
                compressed_string += char
                previous_char = char
                current_streak = 1 
            else:
                current_streak += 1 
            if i == len(string) - 1:
                compressed_string += str(current_streak)
        if len(compressed_string) > len(string):
            return string
        return compressed_string

a = Solution()
print(Solution.Compress('aaaaaabbbbbbbbb')) 