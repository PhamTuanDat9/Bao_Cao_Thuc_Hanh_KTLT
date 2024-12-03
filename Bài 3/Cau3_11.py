print("Pham Tuan Dat")
print("235752021610105")
def benefit(t, n, k):
    for month in range(k):
        n += n * (t / 100)
    return n
try:
    t = float(input("Nhap lai suat tiet kiem (t%/thang):"))
    n = float(input("Nhap von ban dau (n):"))
    k = int(input("Nhap so thang gui (k):"))
    so_tien_nhan_duoc = benefit(t, n, k)
    print(f"So tien nhan duoc sau {k} thang: {so_tien_nhan_duoc:.2f}")
except ValueError:
    print("Vui long nhap so hop le.")
