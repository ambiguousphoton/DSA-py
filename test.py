from timeit import default_timer as timer
import random

arr = [random.randint(0,1000) for i in range(10000000)]
s = timer()
arr.sort() # Nlog(n)
e = timer()
print(e - s)

# def linearSearch(arr,target): # O(N)
#     i = 0
#     while i < len(arr):
#         if arr[i] == target:
#             return i
#         i += 1
#     return -1 

# st = timer()
# ls = linearSearch(arr,100)
# ed = timer()

# print("This is result of linear search",ls,"with time taken", st - ed)

# def binarySearch(arr, target):
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             r = mid - 1 
#         else:
#             l = mid + 1
#     return -1

# st2 = timer()
# bs = binarySearch(arr, 100)
# ed2 = timer()
# print("This is binary search result",bs,"with time taken", st2 - ed2)

# print(   0.22   )
# print(0.0000182 )
