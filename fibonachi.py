def fibonachi(n):
    if n == 0:return 1
    return n * fibonachi(n - 1)

if __name__ == "__main__":
    print(fibonachi(10))