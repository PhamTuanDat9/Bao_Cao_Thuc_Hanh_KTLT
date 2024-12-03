print("Pham Tuan Dat")
print("235752021610105")
str=input("nhap chuoi: ")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict [n] +=1
    else:
        dict [n] = 1
print (dict)
