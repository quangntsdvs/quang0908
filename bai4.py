def powerOfTwoIt(n): #ịnh nghĩa một hàm có tên là powerOfTwoIt nhận một tham số là n.
    i = 0 #Khởi tạo một biến i với giá trị là 0, sẽ được sử dụng để theo dõi số lần lặp.
    power = 1 #Khởi tạo một biến power với giá trị là 1, sẽ được sử dụng để tính lũy thừa của 2.
    while i < n:#Bắt đầu vòng lặp while. Lặp lại các lệnh bên dưới cho đến khi i không còn nhỏ hơn n.
        power = power * 2#Cập nhật giá trị của power bằng cách nhân nó với 2.
        i = i + 1#Tăng giá trị của i lên 1 sau mỗi lần lặp.
    return power#Trả về giá trị của power sau khi vòng lặp kết thúc. Kết quả sẽ là 2^n, nơi n là tham số đầu vào của hàm.