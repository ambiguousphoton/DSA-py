class Solution:
  
# "kdfjklj a sdfklsjklfjklsdjfkl b kdfkjdkjf b fjsdjfklsdjklf a"  
  
    def longest_substring(string):
        char_arr = [0 for i in range(128)]
        for i in string:
            char_arr[ord(i)] += 1
        ends = set()
        for i in range(len(char_arr)):
            if char_arr[i] > 1:
                ends.add(chr(i))
        distance = -1
        for i in range(len(string)):
            pointer = i + 1 
            while pointer < len(string):
                if string[i] == string[pointer]:
                    if distance < (pointer - i):
                        distance = pointer - i
                pointer += 1


        return distance - 1
    
print(Solution.longest_substring("asbsdsdbfda"))