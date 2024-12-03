print("Pham Tuan Dat")
print("235752021610105")
#giai pt tong quat
a= float(input("nhap a (a<>0):"))
b= float(input("nhap b :"))
c= float(input("nhap c :"))
delta=b*b-4*a*c
if delta==0:
    print("pt co nghiem kep x1-x2=",-b/(2*a))
if delta>0:
    print("The equation has 2 distinct solutions xl=",(-b+delta**0.5/(2*a), "and x2=", (-b-delta**0.5/(2*a))))
if delta<0:
    print("ptvn")
