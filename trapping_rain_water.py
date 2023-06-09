class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)  
        mxLeft = 0
        mxRight = 0
        lHts = [0 for i in height]
        rHts = [0 for i in height]
        result = 0
        for i in range(l):
            lHts[i] = mxLeft
            mxLeft = max(mxLeft, height[i])
    
        for i in range(l - 1, -1, -1):
            rHts[i] = mxRight
            mxRight = max(mxRight, height[i])
        
        lowHts = [min(lHts[i], rHts[i]) for i in range(l)]
        print(lHts,rHts,lowHts)
        for i in range(l):
            if lowHts[i] - height[i] > 0:
                result += lowHts[i] - height[i]
        
        return result
