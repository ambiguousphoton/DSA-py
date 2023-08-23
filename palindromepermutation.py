class Solution:
    def is_permutation_of_palindrome(string) -> bool:
        char_counts = [0 for i in range(128)] 
        for char in string:
            char_counts[ord(char)] += 1

        odd_count = 0
        for char_index in char_counts:
            if odd_count > 1:
                return False
            if char_index % 2 != 0:
                odd_count += 1
        return True
a = Solution()
print(Solution.is_permutation_of_palindrome("taco  cat"))
