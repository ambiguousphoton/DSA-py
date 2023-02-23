class Solution:
    def mySqrt( x ) -> int:
        low = 0
        high = 1
        rng = high
        mut,middle = 0,0
        while low<=high:
            middle =  (low + high)/2
            mut = middle*middle
            if mut == x:
                break
            if mut > x:
                high = middle - 1
            if mut < x:
                low = middle +1
        return middle

print(Solution.mySqrt(2015628227))