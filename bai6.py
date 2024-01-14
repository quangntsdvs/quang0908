def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Thử nghiệm đoạn mã
so_lan = 10  # Số lượng số Fibonacci cần tính
ket_qua = [fibonacci(i) for i in range(so_lan)]
print(f"Dãy Fibonacci đầu tiên {so_lan} số là: {ket_qua}")