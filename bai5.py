def giaithua(n): #hàm tên là giaithua nhận một tham số là n.
    if n == 0 or n == 1: #Nếu n là 0 hoặc 1, hàm trả về 1. 
        return 1 #Nếu n không phải là 0 hoặc 1, hàm chuyển sang trường hợp đệ quy. Nó trả về tích của n và giai thừa của n-1.
    else:
        return n * giaithua(n - 1) #Nếu n không phải là 0 hoặc 1, hàm chuyển sang trường hợp đệ quy. Nó trả về tích của n và giai thừa của n-1. 

a = giaithua(8) #Dòng này gọi hàm giaithua với đối số là 8 và gán kết quả vào biến a. Nó tính giai thừa của 8.
print(f"Giai thừa của {8} là: ") 
print(a)
#Lệnh in đầu tiên bao gồm giá trị đầu vào và lệnh in thứ hai in giai thừa đã tính toán.
