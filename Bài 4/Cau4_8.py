print("Pham Tuan Dat")
print("235752021610105")
words = input('Nhap day cac tu: ').split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Tu dai nhat trong day:", ' '.join(longest_words))
