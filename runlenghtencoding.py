a = [
    ['bbbbbwwwbbwwwbwbwbbbbwwbbbwwbwbwbbbbwwbbwbbwbbbbbwwbbbwbbbbwbbwwwbbbb'],
    ['wwwbbbwbbwbwbbwbwbwwwwwwbbbwwwbbbwwwbbbwwwbbbbbwwwbbbwwwbbbwbbwbbwbww'],
    ['bbbbbbbwbwwwbbwwwwbbwbwbbwbwwwwwwwbbwwwwwbbbbbbwwwbbbwbbbbwwwbbbbwbbw'],
    ['bbbbwwbbwbbwbbbbbbbwwwwbbbbbbwwwwbbbbbwwwwwwwwwwbbbwbbwbbwbwbbwbbbbbb'],
    ['bbwbbwbwbwbbwbwbbwbwwbbwbwbwwwwwbbbbwbwbbwbwbwbbwbwbwbbwbwwwwwwwwbbbb'],
    ['wbwwwwwbbbwwwwbbbwwwwwwbbbbbwbbbbbbwwwwwwbbbbbbwwwwwwbbbbwwwwbbbbbwww'],
    ['bbbbbbbwbwwwbbwwwwbbwbwbbwbwwwwwwwbbwwwwwbbbbbbwwwbbbwbbbbwwwbbbbwbbw'],
    ['bbbbwwbbwbbwbbbbbbbwwwwbbbbbbwwwwbbbbbwwwwwwwwwwbbbwbbwbbwbwbbwbbbbbb'],
    ['bbwbbwbwbwbbwbwbbwbwwbbwbwbwwwwwbbbbwbwbbwbwbwbbwbwbwbbwbwwwwwwwwbbbb'],
    ['wbwwwwwbbbwwwwbbbwwwwwwbbbbbwbbbbbbwwwwwwbbbbbbwwwwwwbbbbwwwwbbbbbwww'],
    ['bbbbbbbwbwwwbbwwwwbbwbwbbwbwwwwwwwbbwwwwwbbbbbbwwwbbbwbbbbwwwbbbbwbbw'],
    ['bbbbwwbbwbbwbbbbbbbwwwwbbbbbbwwwwbbbbbwwwwwwwwwwbbbwbbwbbwbwbbwbbbbbb'],
    ['bbwbbwbwbwbbwbwbbwbwwbbwbwbwwwwwbbbbwbwbbwbwbwbbwbwbwbbwbwwwwwwwwbbbb'],
    ['wbwwwwwbbbwwwwbbbwwwwwwbbbbbwbbbbbbwwwwwwbbbbbbwwwwwwbbbbwwwwbbbbbwww'],]
prev = ""
counter = 0
result = ""
for row in a:
    for col in row[0]:
        if prev == col:
            counter += 1
        else:
            result += str(counter)
            counter = 1
            prev = col
result += prev + str(counter)
print(len(result[1::]))
