print("Pham Tuan Dat")
print("235752021610105")
def dem_chu_cai_va_chu_so(cau):
    dem_chu_cai = sum(c.isalpha() for c in cau)
    dem_chu_so = sum(c.isdigit() for c in cau)
    return dem_chu_cai, dem_chu_so
nhap_cau = input("Nhập một câu: ")
chu_cai, chu_so = dem_chu_cai_va_chu_so(nhap_cau)
print(f"Số chữ cái là: {chu_cai}")
print(f"Số chữ số là: {chu_so}")

