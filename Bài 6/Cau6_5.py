print("Pham Tuan Dat")
print("235752021610105")
class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        
        words = self.text.split() 
        return ' '.join(reversed(words)) 

input_string = "hello .py"
reverse_string = ReverseWords(input_string)
output_string = reverse_string.reverse_words()

print("Dữ liệu vào:", input_string)
print("Đầu ra:", output_string)

