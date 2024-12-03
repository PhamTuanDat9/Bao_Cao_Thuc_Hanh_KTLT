print("Pham Tuan Dat")
print("235752021610105")
so_du = 0
while True:
    giao_dich = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ")
    if not giao_dich:
        break
    loai, so_tien = giao_dich.split()
    so_tien = int(so_tien)
    if loai == "D":
        so_du += so_tien  
    elif loai == "W":
        so_du -= so_tien 

print("Số dư thực có trong tài khoản là:", so_du)
