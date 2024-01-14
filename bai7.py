def sum_of_digits(n):#Hàm sum_of_digits nhận một số nguyên dương n làm tham số.
     # Trường hợp cơ bản: khi n là số có một chữ số
    if n < 10:
        return n 
    # Trường hợp đệ quy: tính tổng các chữ số theo cách đệ quy
    else:
        return n % 10 + sum_of_digits(n // 10)
    #Nếu n không phải là số có một chữ số, hàm tính tổng của chữ số cuối cùng (n % 10) 
    #và tổng của các chữ số còn lại bằng cách thực hiện một cuộc gọi đệ quy với phần nguyên của n khi chia cho 10 (n // 10).