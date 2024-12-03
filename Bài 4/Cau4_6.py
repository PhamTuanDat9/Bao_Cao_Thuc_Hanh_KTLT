print("Pham Tuan Dat")
print("235752021610105")
full_name = input("Nhập họ và Tên")
name_parts = full_name.split()
if len (name_parts) >= 2: 
  last_name = name_parts [0]
  first_name = name_parts [1]
  print("Họ:", last_name)
  second_name = name_parts [2]
  print("Tên:",second_name)
else:
  print("String does not have full name.")
