print("Pham Tuan Dat")
print("235752021610105")
nhap_danh_sach = input("Nhập các số, phân tách bằng dấu phẩy: ")
danh_sach = [int(num) for num in nhap_danh_sach.split(",")]
so_le = [num for num in danh_sach if num % 2 != 0]
print("Các số lẻ là:", ', '.join(map(str, so_le)))
