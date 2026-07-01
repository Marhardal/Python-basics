loc = input("Enter File Name:")
fh = open(loc)
lst = list()
count = 0
for line in fh:
    sentence = line.split()
    # print(sentence)
    # break
    if "From" in sentence:
        mail = sentence[1]
        # if mail not in lst:
        count += 1
        print(mail)
        # break
        lst.append(mail)

print('There were '+str(count)+' lines in the file with From as the first word')