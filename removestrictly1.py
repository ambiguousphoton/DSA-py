class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        prev = float("-inf")
        irr = []
        for i in range(len(nums)):
            if not (nums[i] > prev):
                irr.append(nums[i])
                nums.pop(i)
                break
            prev = nums[i]
        prev = float("-inf")
        for i in range(len(nums)):
            if not (nums[i] > prev):
                irr.append(nums[i])
                return False
            prev = nums[i]
            
        print(irr)
        return True
        
