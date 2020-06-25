# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    lines=line.rstrip() #to strip extra line
    uline=lines.upper() #to make all characters in uppercase.
    print(uline)