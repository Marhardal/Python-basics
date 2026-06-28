# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
    read = fh.read()
    print(read.rstrip().upper())
except:
    print("Failed to open your file.")