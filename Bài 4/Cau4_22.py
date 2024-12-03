print("Pham Tuan Dat")
print("235752021610105")
def tat_ca_so_chan(num):
    return all(int(digit) % 2 == 0 for digit in str(num))
chu_so_chan = [num for num in range(1000, 3001) if tat_ca_so_chan(num)]
print("Các số có tất cả các chữ số là số chẵn:", ', '.join(map(str, chu_so_chan)))

