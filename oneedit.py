class Solution:
    def one_edit(self, string1, string2):
        dif = abs(len(string1) - len(string2))
        if dif > 1: return False # more than 1 edits
        if dif == 0: # if replaces are there
            changes = 0
            for char1, char2 in zip(string1, string2):
                if changes > 1:
                    return False
                if char1 != char2:
                    changes += 1
        else: # if inserts or deletes are there
            if len(string2) > len(string1):
                string1, string2 = string2, string1
            p1, p2 = 0, 0
            while p1 < len(string1) and p2 < len(string2):
                if string1[p1] != string2[p2]:
                    p1 += 1
                else:
                    p1 += 1
                    p2 += 1

        return True
a = Solution()
print(a.one_edit('pale','ple'))
print(a.one_edit('pales','pale'))
print(a.one_edit('pales','bale'))
print(a.one_edit('pa','pale'))