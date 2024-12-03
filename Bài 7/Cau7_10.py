print("Pham Tuan Dat")
print("235752021610105")
def find_longest_words(text):
    words = text.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words, max_length
def read_text_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.")
        return None
def main():
    file_name = input("Enter file name to find longest word: ").strip()
    text = read_text_from_file(file_name)
    if text:
        longest_words, max_length = find_longest_words(text)   
        print(f"Longest words in text (length {max_length} characters):")
        for word in longest_words:
            print(word)
if __name__ == "__main__":
    main()
