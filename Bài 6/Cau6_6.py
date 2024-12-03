print("Pham Tuan Dat")
print("235752021610105")
class StringManipulator:
    def __init__(self):
        self.user_string = ""
    def get_String(self):
        
        self.user_string = input("Nhập chuỗi: ")

    def print_String(self):
        
        print(self.user_string.upper())

# Ví dụ sử dụng
string_obj = StringManipulator() 
string_obj.get_String()  
string_obj.print_String()  
