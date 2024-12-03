print("Pham Tuan Dat")
print("235752021610105")
def fibonacci_list(n):
    fibonacci = [0, 1]
    while True:
        next_fib = fibonacci[-1] + fibonacci[-2] 
        if next_fib >= n:
            break
        fibonacci.append(next_fib)
    return fibonacci

n = int(input("Nhập số n: "))
print("Danh sách các số Fibonacci nhỏ hơn", n, "là:", fibonacci_list(n))
