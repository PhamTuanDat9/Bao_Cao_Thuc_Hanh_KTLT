print("Pham Tuan Dat")
print("235752021610105")
def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line)
file_read_from_head('D:/a.txt',1)
