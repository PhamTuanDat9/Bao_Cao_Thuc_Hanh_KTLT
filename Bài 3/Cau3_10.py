print("Pham Tuan Dat")
print("235752021610105")
import math
def Tinh (R):
     if R <= 0:
        return "Ban kinh khong hop le! Vui long nhap ban kinh duong."
     chu_vi = 2 * math.pi * R
     dien_tich = math.pi * R ** 2
     return chu_vi , work_day
try:
   R= float(input("Enter radius R: "))
   ket_qua = Tinh(R)
   if isinstance (ket_qua, tuple):
       print (f"Chu vi hinh tron: {result[0]:.2f}")
       print (f"Dien tich hinh tron: {ket_qua [1]:.2f}")
   else:
       print(ket_qua)
except ValueError:
   print("Vui long nhap mot so hop le.")
