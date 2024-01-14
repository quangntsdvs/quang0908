def recursiveMethod(n):
    if n < 1: #Kiểm tra nếu n nhỏ hơn 1.
        print("n is less than 1") #Nếu n nhỏ hơn 1, in ra màn hình thông điệp "n is less than 1".
    else: # Nếu n không nhỏ hơn 1, thực hiện lệnh bên dưới.
        recursiveMethod(n - 1) #Gọi lại chính hàm recursiveMethod với tham số giảm đi 1. Điều này tạo ra một cuộc gọi đệ quy và tiếp tục đến khi n trở nên nhỏ hơn 1.
        print(n) #Sau khi thoát khỏi cuộc gọi đệ quy, in ra giá trị của n. Điều này sẽ in ra các giá trị từ n đến 1, vì mỗi lần gọi đệ quy giảm giá trị của n đi 1.
