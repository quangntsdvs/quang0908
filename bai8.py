def power(base, exponent):
    # Trường hợp cơ bản: khi số mũ bằng 0, kết quả là 1
    if exponent == 0:
        return 1
    # Trường hợp đệ quy: tính lũy thừa theo cách đệ quy
    else:
        return base * power(base, exponent - 1)