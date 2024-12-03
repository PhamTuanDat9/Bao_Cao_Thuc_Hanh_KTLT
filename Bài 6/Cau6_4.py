print("Pham Tuan Dat")
print("235752021610105")
class RomanToInt:
    def __init__(self):
        self.roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    def convert(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_map[char]
            
            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total

roman_number = "MCMXCIV"  
converter = RomanToInt()
result = converter.convert(roman_number)
print(f"Số nguyên tương ứng với La Mã {roman_number} là {result}")

