print("Pham Tuan Dat")
print("235752021610105")
def count_file_details(file_name):
    try:
        with open(file_name, 'r') as file:
            num_lines = 0
            num_words = 0
            num_characters = 0
            for line in file:
                num_lines += 1 
                num_characters += len(line)  
                num_words += len(line.split()) 
            print(f"Số dòng trong tệp: {num_lines}")
            print(f"Số từ trong tệp: {num_words}")
            print(f"Số ký tự trong tệp: {num_characters}")
    
    except FileNotFoundError:
        print(f"Tệp '{file_name}' không tồn tại. Vui lòng kiểm tra lại tên tệp.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
def main():
    file_name = input("Nhập tên tệp cần kiểm tra: ").strip()
    count_file_details(file_name)
if __name__ == "__main__":
    main()
