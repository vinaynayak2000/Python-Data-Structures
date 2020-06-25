#Enter input as nothing or blank 
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if(line.startswith('From:')):
       continue
    elif(line.startswith('From')):
        f=line
        word=f.split()
        o=word[1]
        count=count+1
        print(o)

print("There were", count, "lines in the file with From as the first word")