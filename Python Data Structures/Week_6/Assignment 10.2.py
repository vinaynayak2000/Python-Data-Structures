name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if(line.startswith('From:')):
       continue
    elif(line.startswith('From')):
        f=line
        word=f.split()
        o=word[5]
        s=o.split(":")
        aword=s[0]
        d[aword]=d.get(aword,0)+1


lst=list()        
for value,count in d.items():
    lst.append((value,count))


lst.sort()
for value,count in lst:
    print(value,count)