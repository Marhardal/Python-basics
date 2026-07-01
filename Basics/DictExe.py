loc = input("Enter File Name:")
fh = open(loc)
dict = dict()
for line in fh:
    sentence = line.split()
    if "From" in sentence:
        mail = sentence[1]
        if mail in dict.keys():
            dict[mail] += 1
            continue
        dict[mail] = 1

bigname = None
bigcount = 0

for key, item in dict.items():
    if bigcount < item:
        bigcount = item
        bigname = key

print(bigname, str(bigcount))