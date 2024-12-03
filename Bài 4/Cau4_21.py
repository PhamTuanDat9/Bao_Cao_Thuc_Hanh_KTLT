print("Pham Tuan Dat")
print("235752021610105")
def is_divisible_by_5(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value % 5 == 0
input_string = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
binary_numbers = input_string.split(',')
divisible_by_5 = [binary for binary in binary_numbers if is_divisible_by_5(binary)]
if divisible_by_5:
    print("Các số nhị phân chia hết cho 5:", ', '.join(divisible_by_5))
else:
    print("Không có số nhị phân nào chia hết cho 5.")


