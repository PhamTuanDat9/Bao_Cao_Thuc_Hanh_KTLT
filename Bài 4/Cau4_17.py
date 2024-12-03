print("Pham Tuan Dat")
print("235752021610105")
def tong_cua_uoc_so(n):
    for i in range(1, n):
        tong_uoc=0
        for j in range(1, i+1):
            tong_uoc +=j
    if tong_uoc> 1:
            print(i)
n=int(input("nhap so nguyen duong n: "))
tong_cua_uoc_so(n)
