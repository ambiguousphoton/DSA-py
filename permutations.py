class Solution:
    def Permutations(self,nums: list[list[int]]) -> list[int]:
        result = []

        if len(nums) == 1:
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.Permutations(nums)
            for perm in perms:
                perm.append(n)
                
            result.extend(perms)
            nums.append(n)
        
        return result

a = [1,2,3]
m = Solution()
print(m.Permutations(a))