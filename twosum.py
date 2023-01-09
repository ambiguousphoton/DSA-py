class Solution:
    def twoSum(self, nums, target): 
        n = 0
        m = len(nums) - 1
        head = nums[n]
        tail = nums[m]
        
        while(True):
            sum_ = head + tail 
            if sum_ == target:
                return [n,m]
            elif sum_ < target:
                n += 1
                head = nums[n]
            else :
                m -= 1
                tail = nums[m]
            
            # if n == m:
            #     return 


