print("Pham Tuan Dat")
print("235752021610105")
def file_read(fname):
    from itertools import islice
    with open (fname, "w") as myfile:
        myfile.write("python exercise\n")
        myfile.write("Java exercise")
    txt = open (fname)
    print (txt.read())
file_read('a.txt')
