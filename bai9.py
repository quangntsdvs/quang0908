def tim_uscn(a, b):
    if b == 0:
        return a
    else:
        return tim_uscn(b, a % b)

# Thử nghiệm đoạn mã
so1 = 48
so2 = 18
uscn = tim_uscn(so1, so2)
print(f"USCN của {so1} và {so2} là {uscn}")