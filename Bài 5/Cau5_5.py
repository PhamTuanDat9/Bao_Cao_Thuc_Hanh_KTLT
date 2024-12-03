print("Pham Tuan Dat")
print("235752021610105")
import numpy as np

# Tạo mảng với các giá trị từ 12 đến 37
mang = np.arange(12, 38)

# Đảo ngược mảng
mang_nguoc = mang[::-1]

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất
vi_tri_max = np.argmax(mang_nguoc)
vi_tri_min = np.argmin(mang_nguoc)

# In ra kết quả
print("Mảng sau khi đảo ngược:", mang_nguoc)
print("Vị trí phần tử lớn nhất:", vi_tri_max)
print("Vị trí phần tử nhỏ nhất:", vi_tri_min)
