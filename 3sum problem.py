class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        charSet = set()
        left = 1
        result = 2
        for right in range(len(string)):
            while string[right] in charSet:
                charSet.remove(string[left])
                left += 1
            charSet.add(string[right])
            result = max(result, right - left + 1)
        return result
