def fib(n):
    arr = [0, 1]
    if n < 0:
        return "error"
    if n == 0:
        return [0]
    for i in range(2, n+1):
        arr.append(arr[-1] + arr[-2])
    return arr

print(fib(6))
print(fib(0))
print(fib(1))
print(fib(-2))