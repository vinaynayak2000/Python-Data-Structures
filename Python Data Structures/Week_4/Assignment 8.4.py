fname = input("Enter file name: ")
fh = open(fname)
lst = list()                     # list for the desired output
for line in fh:                  # to read every line of file romeo.txt
    word=line.strip()            # to eliminate the unwanted whitespaces 
    pieces=word.split()          # line into a list of words
    for element in pieces:       # check every element in word 
        if element in lst:       # if element is repeated
            continue             # do nothing
        else:                    # else if element is not in the list
            lst.append(element)  # append    
lst.sort()                       #sorts the list in ascending order
print(lst)                       # print the list

    