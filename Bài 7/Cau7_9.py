print("Pham Tuan Dat")
print("235752021610105")
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()
        with open(destination_file, 'w') as dest:
            dest.write(content)
        print(f"Copied contents from '{source_file}' to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"The source file '{source_file}' does not exist. Please check again.")
    except Exception as e:
        print(f"An error occurred: {e}")
def main():
    source_file = input("Enter source file name: ").strip()
    destination_file = input("Enter destination file name: ").strip()
    copy_file(source_file, destination_file)
if __name__ == "__main__":
    main()
