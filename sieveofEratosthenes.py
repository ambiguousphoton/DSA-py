
class Solution:
    def countPrimes(self, n: int) -> int:
        array = [True for i in range(n)]
        p1 = 2
        result = 0
        while p1 < n:
            if array[p1] :
                p2 = p1
                for i in range(p1,n):
                    if p1 * i >= n  : break
                    array[p1 * i] = False
                result += 1
            p1 += 1
        return result
