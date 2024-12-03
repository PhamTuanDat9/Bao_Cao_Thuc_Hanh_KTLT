print("Pham Tuan Dat")
print("235752021610105")
def write_list_to_file(file_name, data_list):
    try:
        with open(file_name, 'w') as file:
            for item in data_list:
                file.write(item + '\n')
        print(f"The list contents were written to file '{file_name}' Thành công.")
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")
def main():
    data_list = [
        "Line 1",
        "Line 2",
        "Line 3"
    ]
    file_name = input("Enter the file name you want to write to: ").strip()
    write_list_to_file(file_name, data_list)
if __name__ == "__main__":
    main()
