print("Pham Tuan Dat")
print("235752021610105")
def dem_chu_hoa_va_thuong(cau):
    dem_chu_hoa = sum(c.isupper() for c in cau)
    dem_chu_thuong = sum(c.islower() for c in cau)
    return dem_chu_hoa, dem_chu_thuong
nhap_cau = input("Nhập một câu: ")
chu_hoa, chu_thuong = dem_chu_hoa_va_thuong(nhap_cau)
print(f"Số chữ hoa là: {chu_hoa}")
print(f"Số chữ thường là: {chu_thuong}")
