def firstMethod(): #Định nghĩa hàm đầu tiên.
 secondMethod() 
 print("I am the first Method") #Trong hàm này, gọi hàm secondMethod và sau đó in ra màn hình thông điệp "I am the first Method".
def secondMethod(): #Định nghĩa hàm thứ hai.
 thirdMethod()
 print("I am the second Method") #Trong hàm này, gọi hàm thirdMethod và sau đó in ra màn hình thông điệp "I am the second Method".
def thirdMethod(): # Định nghĩa hàm thứ ba.
 fourthMethod() #Trong hàm này, gọi hàm fourthMethod và sau đó in ra màn hình thông điệp "I am the third Method".
 print("I am the third Method")
def fourthMethod(): #Định nghĩa hàm thứ tư.
 print("I am the fourth Method") #Cuối cùng, gọi hàm firstMethod để bắt đầu chuỗi gọi hàm. Khi hàm này được gọi, nó sẽ kích hoạt chuỗi các hàm khác theo thứ tự đã định nghĩa, và thông điệp sẽ được in ra màn hình theo đúng thứ tự đó.