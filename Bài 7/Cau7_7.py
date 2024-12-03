print("Pham Tuan Dat")
print("235752021610105")
import sys
def count_lines_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"The number of lines in file '{file_name}' is: {line_count}")
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist. Please check the file name again.")
    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    file_name = input("Enter file name to count lines: ").strip()
    count_lines_in_file(file_name)
if __name__ == "__main__":
    main()
