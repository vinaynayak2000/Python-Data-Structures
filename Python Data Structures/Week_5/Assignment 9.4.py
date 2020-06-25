#Enter input as nothing or blank 
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
counts = {}
for line in fh:
    #if(line.startswith('From:')):
     #  continue
    if(line.startswith('From')):
        f=line
        word=f.split()
        o=word[1]
        for word in o:
           counts[word] = counts.get(word,0) + 1
print('Counts', counts)






















