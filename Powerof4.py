# def PowerOF4(num):
#     while num>1:
#         num = num / 4
#     if num == 1:return True
#     else:return False

# print(PowerOF4((4**4)+1))


 #  devide 2 integers
# def devide(dividend,divisor):
#     mul = 1
#     if dividend<0: 
#         dividend=abs(dividend)
#         mul *= -1
#     if divisor<0:
#         divisor =abs(divisor)
#         mul *= -1
#     div = (dividend // divisor) * mul
#     return div
# print(devide(-2147483648,-1))


# 3rd max num
def thirdmax(lst):
    lst = [*set(lst)]
    lst.sort()
    print(lst)
    if len(lst) < 3:
        return lst[-1]        
    return lst[-3]

print(thirdmax([-1,2,3]))