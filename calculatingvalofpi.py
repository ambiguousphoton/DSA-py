import random
no_of_points = int(input("input no. of points :: "))
pi,circle_points,square_points = 0,0,0

for i in range(0,no_of_points):
    x = random.random()*no_of_points  / no_of_points
    y = random.random()*no_of_points / no_of_points
    origin_distance = x**2 + y**2
    if origin_distance <= 1:
        circle_points += 1
    square_points += 1
    pi = (4*circle_points)/square_points

print(f'estimation of pi = {pi}')