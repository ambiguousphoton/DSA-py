class Solution:
    def nearest_neighbour_bigger_than_me(arr:list[int]) -> list[int]:
        result = []
        for i in range(len(arr)):
            right = None
            ri_p = 0
            for index in range(i+1, len(arr)):
                if arr[index] > arr[i]:
                    right = arr[index]
                    ri_p = index
                    break
            # print(result)
            
            left = None
            le_p = 0
            for index in range(0, i):
                if arr[index] > arr[i]:
                    left = arr[index]
                    le_p = index    

            if not left and not right:
                result.append(-1)
            else:
                if abs(i - le_p) <  abs(ri_p - i) and left:
                    result.append(left)
                else:
                    # print(right,left)
                    result.append(right)
        return result
    
print(Solution.nearest_neighbour_bigger_than_me([999,12,4324,2,111,23,999,999,999,999,999,999,0]))