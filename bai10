def decimal_to_binary(n): #hàm decimal_to_binary nhận một số thập phân n làm đối số.
    if n > 1: #trường hợp cơ bản là khi n nhỏ hơn hoặc bằng 1.
        decimal_to_binary(n // 2) #trong trường hợp đệ quy, hàm gọi chính nó với n // 2, và sau đó in ra phần dư khi n chia cho 2 (n % 2).
    print(n % 2, end='') # end='' trong câu lệnh print được sử dụng để in các chữ số nhị phân trên cùng một dòng.

#ví dụ sử dụng hàm với một số thập phân
decimal_number = 25
print(f"Biểu diễn nhị phân của {decimal_number}: ", end='')
decimal_to_binary(decimal_number)
